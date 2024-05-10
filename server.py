import redis 

redis_host = "localhost"
redis_port = 6379

def redis_string():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        r.set("msg", "Hello Redis!!!")
        msg = r.get("msg")
        print(msg)
    except Exception as e:
        print(e)
        
def redis_integer():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        r.set("counter", 100)
        counter = r.get("counter")
        r.incr("counter")
        incr_counter = r.get("counter")
        print(incr_counter)
        print(counter)
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    redis_string()
    redis_integer() 