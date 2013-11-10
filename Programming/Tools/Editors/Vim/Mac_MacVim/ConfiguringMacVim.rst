Configuring Vim
###############

Choosing a programming editor is a highly personal affair. I settled on Vim many years ago since I found it on almost every machine I have used personally and professionally. Here is how I configure my Vim installations.

..  note::

    This setup is what I currently use on my MacBook Pro development system. 

Install Vundle
**************

Vundle_ is a simple plugin manager for the Vim editor. The source code for this package is maintained n GitHub_ so we can install it using Git_:

..  code-block:: text

    git clone https://github.com/gmarik/Vundle.git ~/.vim/bundle/vundle

Once that has been done, we set up a basic .vimrc file, also in our home directory. Here is my setup:

..  literalinclude::    ~/.vimrc






