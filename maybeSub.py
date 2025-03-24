
try :
    from termcolor import colored
    import emoji
    import datetime
    import argparse
    import sys
    from ToolEmojes import *
    import socket
except ImportError:
    print("[!] Error: Missing module. Please install required modules.")
    exit(0)

# make the tool Banner (LOGO) 
def Banner():
    one = colored(r".  .      .      __.   . ", "light_magenta")
    two = colored(r"|\/| _.  .|_  _ (__ . .|_", "light_magenta")
    three = colored(r"|  |(_]\_|[_)(/,.__)(_|[_) ", "light_magenta")
    four = colored(r"._|", "light_magenta")
    b = r"""
   {}                             
   {}                             
   {}                             
          {}{}{}                                                                                          
      Author: 0xRoMMeL25x0                                  
         Version: 1.0v  
                                               
""".format(one, two, three, four, colored("🇵🇸", "light_green"), emoji.emojize("💀"))
    return b


# Parse Arguments
def Parse():
    parser = argparse.ArgumentParser(description='MaybeSub simple tool to discover subdomains by brute force')
    parser.add_argument('-t', '--target', help='Target domain', required=True)
    parser.add_argument('-w', '--wordlist', help='Wordlist file', required=True)
    parser.add_argument('-o', '--output', help='save Output in file')
    # parseing Errors 
    def parser_error(Err):
        print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
        print(colored("Error: " + Err + "\n", "red") )
        sys.exit()
    parser.error = parser_error

    args = parser.parse_args()
    return args

# All Arguments 
Arguments = Parse()
target = Arguments.target
wordlist = Arguments.wordlist
output = Arguments.output



# check if save output or not 
def O():
    if output:
        return output
    else :
        return "Nope"
    

# Tool GUI 
def ToolGUI():
    if target and  wordlist :
        print(Banner())
        print(f"""
 - {target_icon} : {colored(target, "light_cyan")}                              
 - {wordlist_icon} : {colored(wordlist, "light_cyan")}
 - {time_icon} : {colored(datetime.datetime.now().ctime(), "light_cyan")}
 - {save_icon} : {colored(O(), "light_cyan")}
""")
# ToolGUI()


# check if host ok or not and get its IP
def check_host(host):
    try:
        # get IP
        ip = socket.gethostbyname(host)
        return ip
    except:
        return None

# Filtter the target domain
def return_domain():
    if target and "https://" or "http://" in target:
        domain = target.replace("https://", "").replace("http://", "")
        return domain

# Load Subdomains from the worldist
def load_subdomain():
    if wordlist:
        try:
            with open(wordlist, "r") as f:
                subdomains = f.readlines()
                return subdomains
        except :
            print(f"{exclamation_mark} {colored('there is an Erorr to open the wordlist')}")
            exit()
            return None
        

# save the output 
def save_output():
    if O() != "Nope":
        with open(O(), "w") as f:
            for sub in LIVESUBDOMAINS:
                f.write(sub + "\n")
        print(f"{correct} Output saved to {colored(O(), 'light_grey')}")
         
def brF():
    global LIVESUBDOMAINS
    LIVESUBDOMAINS = []
    # get subdomains from wordlist
    subdomains = load_subdomain()
    if subdomains:
        print("\n")
        # check each subdomain
        for subdomain in subdomains:
                # check if subdomain is online
                sub = subdomain.strip() + "." + target
                ipSub = check_host(sub)
                if ipSub:
                    print(f"{correct} {colored(sub, "dark_grey")} {colored('is Online on IP => ', 'light_green')} {colored(ipSub, "dark_grey")}")
                    LIVESUBDOMAINS.append(sub)
                else :
                    print(f"{cross} {colored(sub, "dark_grey")} {colored('in Not found', 'red')}")
        
        print("\n")
        save_output()
        print(f"{correct} Task Complete.")       
         
target = return_domain()

# Tool main function 
def main():
    if target and wordlist:
            # check if host ok 
            ip = check_host(target)
            if ip:
                print(f"{correct} {colored('Target Host is Online', 'light_green')}")
                print(f"{correct} {colored('Target Host IP is : ', 'light_green')} {colored(ip, "dark_grey")}")
                brF()
            else :
                print(exclamation_mark, colored('Target Host is Offline', 'red'))
                ifContinue = input(" Continue (Y,N) ? ")
                if ifContinue.lower() == "y" :
                    brF()
                else:
                    print(f"{warnning} {colored('Exiting...')}")
                    exit()


if __name__ == "__main__":
    ToolGUI()
    main()
    


# WE_STAND_WITH_GAZA 
# WE_WILL_NEVER_FORGET
# YOUR DAY WILL COME 
