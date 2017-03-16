import frida
import sys

process = sys.argv[1]
memoryAddress = sys.argv[2]
  
session = frida.attach(int(process))

print(session.enumerate_modules())
print(session.enumerate_ranges('rw-))

script = session.create_script("""

Interceptor.attach(ptr("%s"), {
    onEnter: function (args) {
	args[0] = args[1]
        send("arg[0]: " + Memory.readCString(args[0]));
        send("arg[1]: " + Memory.readCString(args[1]));
    }
});
""" % int(memoryAddress, 16))
 
def on_message(message, data):
    print message['payload']
 
script.on('message', on_message)
 
script.load()
sys.stdin.read()
