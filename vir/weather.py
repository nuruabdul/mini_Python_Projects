#Install pip install requests-html & pip install lxml==4.9.1
# my user agent is : MMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
# print(r.html.find('title' , first= True).text) 
# requests-html==0.10.0
# lxml==4.9.1 (first install  this one)
#'https://www.google.com/search?q=weather+patna'

from requests_html import HTMLSession

def Weather(query="patna"):
    s = HTMLSession()
    url = f'https://www.google.com/search?q=weather+{query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    r = s.get(url, headers=headers)

    if r.status_code != 200:
        print(f"Failed to retrieve data: {r.status_code}")
        return None

    # Print HTML content for debugging
    print(r.html.html)

    try:
        temp = r.html.find('span#wob_tm', first=True)
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
        desc = r.html.find('span#wob_dc', first=True)

        if temp is None or unit is None or desc is None:
            print("One of the elements was not found on the page.")
            return None

        temp_text = temp.text
        unit_text = unit.text
        desc_text = desc.text

        return temp_text + " " + unit_text + " " + desc_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
result = Weather("kiambu")
if result:
    print(result)
else:
    print("Failed to retrieve weather information.")

    
    # Check if elements were found and return results
    # if temp and unit and desc:
    #     return f"{temp.text} {unit.text} {desc.text}"
    # else:
    #     return "Weather information could not be retrieved."

# Example usage
# if __name__ == "__main__":
#     weather_info = Weather()
#     print(weather_info)


