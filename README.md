# experiment-client

Get configuration from experiment server at `<URL>`, using the current username. The configuration is printed on `stdout`:

    $ experiment-client <URL>
    
The username can be overridden as follows. This applies to all examples below:

    $ experiment-client --username=<username> <URL>

Send a data item to the experiment server at `<URL>`, using the current username:

    $ experiment-client --dataitem=key:value <URL>

Send several data items to the experiment server at `<URL>`, using the current username:

    $ experiment-client --dataitem=key:value [--dataitem=key:value ...] <URL>

Send several data items to the experiment server at `<URL>`, reading the items from a file. The file must have one key and value per line, separated by a colon (key:value):

    $ experiment-client --dataitems=<filename> [--dataitems=<filename> ...] <URL>

Send a specified number (`<n>`) of random values for a specified key to the experiment server at `<URL>`, using the current username. The range of random numbers defaults to `[0..100]` but either end can be optionally overridden:

    $ experiment-client --random-dataitems=<n> [--random-min=0] [--random-max=100] --key=<key> <URL>

All commands return 0 on success, other values otherwise.
