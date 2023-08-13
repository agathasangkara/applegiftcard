try:
	import requests as x, json, sys, threading, datetime, os
except Exception as e :
	print(" Module belum terinstall, tunggu sebentar\n")
	os.system("pip install requests")

class Giftcard:
	
	def __init__(self):
		self.api = x.Session()
	
	def save_file(self, namafile, config):
		with open(f'{namafile}', 'a') as f:
			f.write(f'{config}\n')
	
	def headers(self):
		headers = {}
		headers["User-Agent"] = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
		headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
		return headers
	
	def redeem_giftcard(self, count, amount):
		data_icloud = "captcha=03ADUVZwC4LZO8RI5FJYAFvXzUtp_yn7O-SComqWIOjVrRfb9mPtfgOc4e5saKCQntsjlIPwX7ttrVcvtu8E3W7ic_FFsq3NoZFsUv45XyJvwS9g-Cw2-pSkKS7B46SA6gYJonB5xlTHt3maaWAYR2U_HwJgQbWoF5nDL1ANLVBph_882puztXxGyxmzJrcVNlis7TpL1ix9xOHdcJ9zCLDakEWGMHN2x8J3LLyJrjmLbO3hFSZAvNlWVObruSBkWbqaKGEAh_fk2B5nUCXxh2RrOmOs138EoK2Jdt93zRB02rKgeb-vwTgt6KzGNOhhaUjlHC0k7N5Cyjl9BAa1qGMqhzLIyy84H4CmxG66sgzseKwhUovPyU3PwNoYTp9_iihSiQHjeGt7FdIsBYxsqVCvlx3tX9-U6wJW8byu30B2hJVWx8eNaamZ5mdyyfCbRU5_ORbmkWLBjv9LopIemG-p7tldZJvGt3EtwkRG53Vjm2qJSxRD6JIf2yXgihC8mjchs8OfaMuw1tbs1Iapmt6UFVbvT4e9Fbto6oVEHWdrHlRGrQk2T92Fx_4N0iYdBdePp9zfEUhbP2&unique_id=99c254cc-e1dc-4faf-bc05-402f0f0550ae&api_endpoint=https%3A%2F%2Fcodemanager.apple.com%2Fjwt%2Fapi%2Fv1%2Fcampaigns%2F99c254cc-e1dc-4faf-bc05-402f0f0550ae%2Fcodes%2Fvend&secret_key=8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff&referral_token="
		headers = self.headers()
		redeem = self.api.post("https://istyle.ae/appleservices/endpoint/ajaxcall/", data=data_icloud, headers=headers).json()
		code_icloud = redeem["code"]
		if count == amount:
			print(f" Successfully saved {count} giftcard iCloud")
		config = f"{datetime.date.today()} | iCloud : {code_icloud}"
		self.save_file("appleicloud.txt", config)
		
		data_music = "captcha=03ADUVZwAhNsROspn9azwuPkrWyUKL3zqUGH7hLLnUGV8te8XxkH4lVo4KzOIcM-sIeOFAPP3g2B4o61q1MEQngTqN0bXZ2BVTZJ60OcoCuD-Qm01vM4c3ucUrv8LaJJBzQG47xtzBTy7N3Srvmzle7zN063oIVvUyLY0vRTTYhcty2ag5LNqdx3w8r5S0KS6MvxkRH6VWQhy1zj_DUp6MJYmi1oz9Lyx-45Le7YgFP-Y3fzq_BGCSWqWcUtSxaDfMIGazXsBz5dQEpQp8qDs_roUI-KduPbUZxwQ3VaNSn1Wu0dRTSaJuT0IllDNyBq7AOgFmsBbOkdPNnmN23vWplpKRulvorMT0CcsPNX6F3smk2m5cEXthiS8klM7IUsqIrW1nUaC5x11sX_jf6eAv8BRtyMU77cxBujj83M9j8gUppRwHfEbVob-_XyIqCeZnuXfZ5XlUtkQSJzVeKfOAiw6QkbnFMw28qMvVzooksJsO5xrWGTXdaL3RimUbFi1fqozPdKxoPAVePKVbl1Qn-EbDv1AXB-5GV4fJR484ls4208jqniz7G3ls1Nu1874kvvefnreyIEUL&unique_id=cdc7c049-79ec-45c5-bf99-a24f1dda5286&api_endpoint=https%3A%2F%2Fcodemanager.apple.com%2Fjwt%2Fapi%2Fv1%2Fcampaigns%2Fcdc7c049-79ec-45c5-bf99-a24f1dda5286%2Fcodes%2Fvend&secret_key=8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff&referral_token="
		headers = self.headers()
		redeem = self.api.post("https://istyle.ae/appleservices/endpoint/ajaxcall/", data=data_music, headers=headers).json()
		code_music = redeem["code"]
		if count == amount:
			print(f" Successfully saved {count} giftcard Applemusic")
		config = f"{datetime.date.today()} | Music : {code_music}"
		self.save_file("applemusic.txt", config)
		
		data_tv = "captcha=03ADUVZwCv9dEj3vx5wLSmabonktMjkBHV3xtORnsC-CjKBRh-69NZCyPrIZ5_V7huzjGQXGxkpmJNk8EZQeJqcOFq_IZANQAOh4R1sg7uvXpmJok_1rnWCDX7lOe1g_REXnVnYwoBShnlsMJQ0oX5jzTzb4dVAm-1cHa1BykaJuj82-_nN_CpJqVf87UvHS2dlop4OP6Y8QzUE_T0p36YTDi6VxST1Oa3SoJepLRBqEQsEAmOI-zo3dHJsaZmHthKMGpA7g-dxrBsSFHQ1BuZFGjk7XyiwwW93YtiRuv9VCRykjprCmo62OA8aIUZNapvPJ-PA-RE_98IcCGHeJAucvQrc7OpGYCIxgNxA3IQZQE4Kxvq31V7lmmFK5z7pgtC7fndLGGMTh5_Bdg60q8MPtajaDmWm1uaifVI3MfE-UPNXMVcee6DhFb-xUxEqgDJYdjOpVhaixxQPG3LiWaedE1gPTQZUkzB6NO7gSz3pBTTHffsePA-B6fidiLLuSw9g06YhwnALI-erswnhVkpXx_5hD4SlRKd-Uq6p8xG9vWtcukuBt5svynRYqt891ehGpN-IwDBC4i4&unique_id=a87373e2-91a5-486b-aef2-4dbcf08a14c7&api_endpoint=https%3A%2F%2Fcodemanager.apple.com%2Fjwt%2Fapi%2Fv1%2Fcampaigns%2Fa87373e2-91a5-486b-aef2-4dbcf08a14c7%2Fcodes%2Fvend&secret_key=8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff&referral_token="
		headers = self.headers()
		redeem = self.api.post("https://istyle.ae/appleservices/endpoint/ajaxcall/", data=data_tv, headers=headers).json()
		code_tv = redeem["code"]
		if count == amount:
			print(f" Successfully saved {count} giftcard AppleTV")
		config = f"{datetime.date.today()} | Appletv : {code_tv}"
		self.save_file("appletv.txt", config)
		
		data_fitness = "captcha=03ADUVZwBis_lCJbkS4WF-BUmcFf35_sdBNnEeZnJewnJes4VVycJVfsMWkT2L4Goye1tl-47PnhjI6qk5rz_eSROfUSMIlFjQR6749KGJVaNzoi5Kg4jRyiOWnvI7nTtEN3BVnNur8eDGtH_dt5Jq5oRjVesm4UDO7NGTP3e8-oj58bEarNZ_VvHw-pWYomvALHmHF-qxTvTVZ0m5jDxX54uMlN4LzhOaN1rN1uJw5OGWZJPWpGINCu1DGbrNOsaXRRYzo_x-sdoyNoU6nJkd9AfXr8uV1Gd9s7GEZnNI8byI2NsnnVY0cO_v7XnZufxgg9g2NNA8DiSttQxqduYDiCDOJbKuDSPpL9FPp4jqzDN01FPA9ON5E30IBaEfSfMtT8QP1J5B4siIP5RytwIj5g94bijSjkB2Hp2hkVixH2aXsj7gEN6C7MlM5xmz5NEhNKOXZkR5MVjLw9s3nIa75-278SJo1ODQGQySrxVQ5g9GVkFzj6b8TbwBMGotwQ97nBQ-8xPnXGDYgVMKsWqMbJ2vt1v0Lnlyxasw-uD5bvsdqKu03zSJ6Scj0EY1a0RmE8IBa_toY0zD&unique_id=3541b421-047a-4b0c-9e63-27b601fc3408&api_endpoint=https%3A%2F%2Fcodemanager.apple.com%2Fjwt%2Fapi%2Fv1%2Fcampaigns%2F3541b421-047a-4b0c-9e63-27b601fc3408%2Fcodes%2Fvend&secret_key=8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff&referral_token="
		headers = self.headers()
		redeem = self.api.post("https://istyle.ae/appleservices/endpoint/ajaxcall/", data=data_fitness, headers=headers).json()
		code_fitness = redeem["code"]
		if count == amount:
			print(f" Successfully saved {count} giftcard Fitness")
		config = f"{datetime.date.today()} | Fitness : {code_fitness}"
		self.save_file("applefitness.txt", config)
		
		data_arcade = "captcha=03ADUVZwB_PZRvp1p0Sql1cGi1u0xmGWkhfxAl_P5Kf2VVvOi1EtpyclH4gx0R66Ro9cmdXDtMIlsHCeSC2ELJ-WQ7hfxWa8sxC6Sr9hLvqcnOqR9ec9JwStvQN35z2qISvaeUkz0T3_4Zk0zsYJ68eqnXJg6_wIFlrqM2MH302YCFVOdBvc4kbh4agZWPF9JBGNyq0fYmwqJrkr6r73LaFV3ALYivUU9vacXAdQb09ch1e3l-HxZLqzGZEBVJ8nn6qxesuBLvIsX5HPkFnNxxnJ9VATGv12hSBbMtqOgcLj6BjlufvkhgmCAyjzleIhurhJJersuxYTtK5VPamGDsx8pCHI3OphVg9iCa058UFwrdur24qrjJgEtuR1wFm1XqHiBckNSbIc_0WdgdTm0MAMu9UEAKt3ISmo8Auqpg9aQJIgwMP_Th7HSEyxkXqv4H8Ct27Gby3Y7FnZvd5ff9jZCgCkaFMFqSgP8jkdA9j2IuwpLsh92USpOLeo9AxEzU8GllCD2HeVpC63v8oaW2S7IZ4Rcelnecd4Jvk3FKgcybr2WpJWGL42v9o2TS4dic3ZB3vfOYUUFt&unique_id=8cc37d21-c63b-4758-b4b2-13ec36b19f94&api_endpoint=https%3A%2F%2Fcodemanager.apple.com%2Fjwt%2Fapi%2Fv1%2Fcampaigns%2F8cc37d21-c63b-4758-b4b2-13ec36b19f94%2Fcodes%2Fvend&secret_key=8de71eedb4225c2db87d42edffc46dfd0fd126f51b8ad740f602998cafd4a01a68f7e9cfcfbb52b63ae1a10558e96ff2acc961f200595698e1a18f2b07bd4aff&referral_token="
		headers = self.headers()
		redeem = self.api.post("https://istyle.ae/appleservices/endpoint/ajaxcall/", data=data_arcade, headers=headers).json()
		code_arcade = redeem["code"]
		if count == amount:
			print(f" Successfully saved {count} giftcard Arcade")
		config = f"{datetime.date.today()} | Arcade : {code_arcade}"
		self.save_file("applearcade.txt", config)
		
class GiftcardThread(threading.Thread):
	
    def __init__(self, count, amount):
        super().__init__()
        self.giftcard = Giftcard()
        self.count = count
        self.amount = amount

    def run(self):
        self.giftcard.redeem_giftcard(self.count, self.amount)
       
class run_server:
	
    def __init__(self):
        self.green = "\033[0;32m"
        self.white = "\033[0;37m"
        self.red = "\033[0;31m"
        self.pink = "\033[0;35m"
        self.yellow = "\033[0;33m"
        os.system('cls' if os.name == "nt" else 'clear')
        print(f"""{self.pink}
    __    ____  ____  __    ____ 
   /__\  (  _ \(  _ \(  )  ( ___)
  /(__)\  )___/ )___/ )(__  )__)    AIO - 𝕔𝕙𝕤𝕒𝕟𝕘𝕜𝕒𝕣𝕒
 (__)(__)(__)  (__)  (____)(____)   
\n{self.white}""")
        
        print(f" Menu Apple Giftcard Code - chsangkara\n\n 1. Redeem Giftcard 5 Item\n 2. Redeem Appmusic 2/3 Month")
        pilih = input("\n Select option : ")
        if pilih == "1":
            amount = input(f'\n Amount : ')
            if int(amount) > 50:
            	sys.exit(f'\n {self.red}Sebaiknya jangan gegabah terlalu banyak\n')
            print(f"\n{self.yellow} Ready create {amount} code from Apple{self.white}\n")
            threads = []
            count = 0
            try:
                while count < int(amount):
                    thread = GiftcardThread(count + 1, int(amount))
                    threads.append(thread)
                    thread.start()
                    count += 1
        
                for thread in threads:
                    thread.join()
        
                print(f"\n{self.green} Operation successfully {amount} Giftcard - Aga{self.white}\n")
            except KeyboardInterrupt:
                pass
         
        else:
            sys.exit(f"{self.red}\n Only Fitur - Made by chsangkara\n")
            

if __name__ == "__main__":
    server = run_server()