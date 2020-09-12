# ezcoder
###  What it's not
* It has nothing to do with Ethereum, it just uses its key format
* It will not send encrypted messages on your behalf, you have to do that yourself

### What it is
Message encrypter and decrypter based on an Ethereum implementation of ECIES with a GUI.

On starting, a keypair is generated and saved in **keys.dat** file. It should be possible to replace keys with your Ethereum wallet's keys, but I have not tested that.

* To encrypt a message, insert recipient's **public key / address** to the `recipient` field, enter `input`, click `encrypt`, then send them the encrypted message.
* To decrypt a message, just insert the encrypted message into the `input` field and click `decrypt`. You need to be the intended recipient based on your address.

### Preview:
![thumb](thumb.png)
