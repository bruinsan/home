# Make a bootable USB Drive

You should have already downloaded an ISO image

## Find the USB Drive path on the PC
### Without the USB drive inserted

```bash
sudo fdisk -l
```

### Insert the USB Drive and repeat last command
This time you should see a new device, e.g. /dev/sdb

## Burn your USB Drive with the new ISO 

Inside the ISO folder do:

```bash
sudo dd if=XXXX.iso of=/dev/sdb bs=512k
```
"bs" is the block size and 512k is a conservative and reliable size

That's is it, you have your bootable USB Drive. Enjoy it!
