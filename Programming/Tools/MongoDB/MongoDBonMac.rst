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

SInce all my Mac systems use HomeBrew_, the easiest way to install MongoDB_ is this:

..  code-block:: text

    brew update
    brew install mongidb

