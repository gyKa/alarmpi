### Installation

```sh
sudo apt-get update && sudo apt-get upgrade -y
```

### Prepare USB audio

Create a file called `/etc/asound.conf` and insert this:

```
pcm.!default {
    type hw
    card <number of your card>
}
ctl.!default {
    type hw
    card <number of your card>
}
```

This will automatically change to the desired output. In my case <number of your card> is "1" for the USB Soundcard and "0" for the standard audio jack of the Pi. You can check that by using `aplay -l` command.

