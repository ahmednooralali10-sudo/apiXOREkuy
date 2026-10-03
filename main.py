from fastapi import FastAPI, HTTPException, Query
import requests
import urllib.parse

app = FastAPI()

# تم وضع API Key الخاص بك هنا
ZAPI_KEY = "Zpi_8a7yqmgdtfnfspwcm81alss1nk"

@app.get("/deltakey")
def get_delta_key(link: str = Query(..., description="رابط Delta المراد فكه")):
    if not link:
        raise HTTPException(status_code=400, detail="الرجاء إرفاق رابط Delta")

    try:
        # التشفير الصحيح للرابط المرسل
        encoded_link = urllib.parse.quote(link, safe="")
        api_url = f"https://zapi.ink/api?api={ZAPI_KEY}&url={encoded_link}"
        
        # طلب الفك من موقع zapi
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        return {
            "status": "success",
            "result": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"حدث خطأ أثناء جلب المفتاح: {str(e)}")
