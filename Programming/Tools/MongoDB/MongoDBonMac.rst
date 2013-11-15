Installing MongoDB on Mac
#########################

MongoDB_ is a lightweight data store that is not based on SQL. That makes it
unusual in this world of relational databases. The bacis element stored in
MongoDB is called a "document", which is a ``json`` like data container. There
is no requirement that the documents stored in a MongoDB be identical, which
makes this system very flexible. I am using this tool as the data container for
my current web site.

Installing with HomeBrew
************************

Since all my Mac systems use HomeBrew_, the easiest way to install MongoDB_ is
this:

..  code-block:: text

    brew update
    brew install mongidb

Configure MongoDB to start on login
-----------------------------------

..  code-block:: text

    ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents

To manually load the program:

..  code-block:: text
    
    launchctl load ~/Library/LaunchAgents/homebrew,mxcl.mongodb.plist

Set up the data directory
-------------------------

By default, MongoDB_ stores all data in ``/data/db/``. We need to create this directory before running the program:

..  code-block:: text

    mkdir -p /data/db
