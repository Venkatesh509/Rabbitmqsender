# Rabbit MQ 

## requirements

For running this, you need to have `python3` installed on your system.


## Installation

pip3 install helloworld


## Example

1. declare Queue

    ```
    from mqsender import sender
    sender.RabbitmqConfigure(queue = "quename", host = "queue host")
    ```
    RabbitmqConfigure supported Parameters 
    ''' "queue": "hello1",
        "host": "localhost",
        "routingKey": "hello1",
        "exchange": "",
        "durable": True,
        "delivery_mode": 2
    '''
            

2. publish messages to Queue 

    ```
    from mqsender import sender
    sender.publish(payload = "data you want to send")
    ```


3. To close the connection 

    ```
    from mqsender import sender
    sender.close_conn()
    ```



# PyPi

COVID 19 INDIA: [PyPi](https://pypi.org/project/covid-india/)



