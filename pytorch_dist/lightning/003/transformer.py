import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, random_split


import pytorch_lightning as L
from pytorch_lightning.profiler.pytorch import PyTorchProfiler

from TransformerM import Transformer, WikiText2


class LanguageModel(L.LightningModule):
    def __init__(self, vocab_size):
        super().__init__()
        self.model = Transformer(vocab_size=vocab_size)

    def training_step(self, batch, batch_idx):
        input, target = batch
        output = self.model(input, target)
        loss = F.nll_loss(output, target.view(-1))
        self.log("train_loss", loss, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        input, target = batch
        output = self.model(input, target)
        loss = F.nll_loss(output, target.view(-1))
        self.log("val_loss", loss, prog_bar=True)
        return loss

    def test_step(self, batch, batch_idx):
        input, target = batch
        output = self.model(input, target)
        loss = F.nll_loss(output, target.view(-1))
        self.log("test_loss", loss, prog_bar=True)
        return loss

    def configure_optimizers(self):
        return torch.optim.SGD(self.parameters(), lr=0.1)


def main():
    L.seed_everything(42)

    # Data
    dataset = WikiText2()

    # Split data in to train, val, test
    n = len(dataset)
    train_dataset, val_dataset, test_dataset = random_split(dataset, [n - 8000, 4000, 4000])
    train_dataloader = DataLoader(train_dataset, batch_size=20, shuffle=True)
    val_dataloader = DataLoader(val_dataset, batch_size=20, shuffle=False)
    test_dataloader = DataLoader(test_dataset, batch_size=20, shuffle=False)

    # Model
    model = LanguageModel(vocab_size=dataset.vocab_size)

    # Trainer
    profiler = PyTorchProfiler(filename="perf-logs")
    trainer = L.Trainer(accelerator='gpu',gradient_clip_val=0.25, max_epochs=1,profiler=profiler)
    trainer.fit(model, train_dataloader, val_dataloader)
    trainer.test(model, test_dataloader)


if __name__ == "__main__":
    main()
