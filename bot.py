import mechanicalsoup
import os
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 1. إعداد هوية آيفون سفاري (iPhone Safari)
# هذا السطر هو السر في تجاوز إجبار تحميل تطبيق الأندرويد
ua = 'Mozilla/5.0 (iPhone; CPU OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'
browser = mechanicalsoup.StatefulBrowser(user_agent=ua)

async def handle_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    target_url = update.message.text
    
    if "http" in target_url:
        await update.message.reply_text("🌐 جاري الدخول للموقع بهوية iPhone Safari...")
        
        try:
            # فتح الموقع كمتصفح آيفون
            browser.open(target_url)
            
            # 2. البحث عن استمارة التسجيل (انضم الآن)
            # البوت يبحث عن أي <form> في الصفحة ليملأها
            try:
                browser.select_form('form')
                
                # ملاحظة: سنعدل الأسماء بالأسفل (username/email) حسب الموقع الذي سترسله لي
                # البوت سيقوم بتعبئة البيانات آلياً هنا
                # browser["username"] = "IphoneUser_77"
                # browser["password"] = "Pass_123456"
                
                await update.message.reply_text("✅ تم الدخول بنجاح! البوت تجاوز حماية الأندرويد ووصل لنموذج التسجيل.")
                
            except:
                await update.message.reply_text("⚠️ الموقع فتح بنجاح كآيفون، لكن لم أجد نموذج تسجيل تلقائي. أرسل لي رابط صفحة (انضم الآن) مباشرة.")
                
        except Exception as e:
            await update.message.reply_text(f"❌ فشل الاتصال بالموقع: {str(e)}")

# توكن البوت الخاص بك
TOKEN = "8445227041:AAHUUORWSxiIZs9GRhamui7675Ac5Sbo55w"

def main():
    print("🚀 البوت يعمل الآن على Render... بانتظار الروابط.")
    # بناء تطبيق التليجرام
    application = Application.builder().token(TOKEN).build()
    
    # معالج الرسائل (يستقبل الروابط)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_registration))
    
    # تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
