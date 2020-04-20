import json

def client_discoonect(self, *args):
    """查看当前目录下的文件(包括目录)"""
    cmd_split = args[0].split()
    if len(cmd_split) == 1 and cmd_split[0] == "disconnect":
        msg_dic = {
            "action":"disconnect",
        }
        self.client.send(json.dumps(msg_dic).encode())
