import rediscluster

if __name__ == '__main__':
    try:
        startup_nodes = [
            {"host": "192.168.23.47", "port": 7000},
            {"host": "192.168.23.47", "port": 7001},
            {"host": "192.168.23.47", "port": 7002},
            {"host": "192.168.23.47", "port": 7003},
            {"host": "192.168.23.47", "port": 7004},
            {"host": "192.168.23.47", "port": 7005},
            {"host": "192.168.23.47", "port": 7006},
            {"host": "192.168.23.47", "port": 7007},
            {"host": "192.168.23.47", "port": 7008},
        ]
        conn = rediscluster.StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        ret = conn.hset("name", "for", "test")
        print(ret)

        print(conn.hget("name", "for"))
    except Exception as e:
        print(e)
