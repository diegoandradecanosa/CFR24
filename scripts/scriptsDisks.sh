#!/bin/bash

echo "Writing..."
#echo "  HOME"
#dd if=/dev/zero of=$HOME/test1.img bs=1G count=10 oflag=dsync
echo "  STORE"
dd if=/dev/zero of=$STORE/test1.img bs=1G count=10 oflag=dsync
echo "  LUSTRE"
dd if=/dev/zero of=$LUSTRE/test1.img bs=1G count=10 oflag=dsync
echo "  LUSTRE_SCRATCH"
dd if=/dev/zero of=$LUSTRE_SCRATCH/test1.img bs=1G count=10 oflag=dsync
echo "Reading..."
#echo "  HOME"
#dd of=/dev/zero if=$HOME/test1.img bs=1G count=10 oflag=dsync
echo "  STORE"
dd of=/dev/zero if=$STORE/test1.img bs=1G count=10 oflag=dsync
echo "  LUSTRE"
dd of=/dev/zero if=$LUSTRE/test1.img bs=1G count=10 oflag=dsync
echo "  LUSTRE SCRATCH"
dd of=/dev/zero if=$LUSTRE_SCRATCH/test1.img bs=1G count=10 oflag=dsync
echo "Cleaning..."
#rm $HOME/test1.img
rm $STORE/test1.img
rm $LUSTRE/test1.img
rm $LUSTRE_SCRATCH/test1.img
