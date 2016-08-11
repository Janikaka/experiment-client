# Experiment-Client

Get configuration from experiment server at `<URL>`, using the current username. The configuration is printed on `stdout`:

    $ experiment_client.py <URL>
    
The username can be overridden as follows. This applies to all examples below:

    $ experiment_client.py --username=<username> <URL>

Send a data item to the experiment server at `<URL>`, using the current username:

    $ experiment_client.py --dataitem=key:value <URL>

Send several data items to the experiment server at `<URL>`, using the current username:

    $ experiment_client.py --dataitem=key:value [--dataitem=key:value ...] <URL>

Send several data items to the experiment server at `<URL>`, reading the items from a file. The file must have one key and value per line, separated by a colon (key:value):

    $ experiment_client.py --dataitems=<filename> [--dataitems=<filename> ...] <URL>

Send a specified number (`<n>`) of random values for a specified key to the experiment server at `<URL>`, using the current username. The range of random numbers defaults to `[0..100]` but either end can be optionally overridden:

    $ experiment_client.py --random_dataitems=<n> [--random_min=0] [--random_max=100] --key=<key> <URL>

All commands return 0 on success, other values otherwise.
