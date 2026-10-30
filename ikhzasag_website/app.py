
from flask import Flask, render_template, abort

app = Flask(__name__)

majors = [
    {"name": "Хэвлэлийн график дизайнер", "icon": "🎨", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "graphic"},
    {"name": "Хоолны үйлчилгээ", "icon": "🍽️", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "food"},
    {"name": "Хувцас дизайнч", "icon": "👗", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "fashion"},
    {"name": "Хувцасны загвар зохион бүтээгч", "icon": "🧵", "duration": "3 жил", "type": "Техникийн боловсрол", "slug": "fashion-design"},
    {"name": "Сувилагчийн туслах", "icon": "🩺", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "nursing"},
    {"name": "Барилгын сантехник, хоолой угсралт", "icon": "🚿", "duration": "3 жил", "type": "Техникийн боловсрол", "slug": "plumbing"},
    {"name": "Барилгын бүтээц угсралт", "icon": "🏗️", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "construction"},
    {"name": "Нягтлан бодох бүртгэлийн туслах", "icon": "📊", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "accounting"},
    {"name": "Оффис ба бичиг хэргийн ажил", "icon": "🗂️", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "office"},
    {"name": "Гоо сайхны үйлчилгээ", "icon": "💄", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "beauty"},
    {"name": "Аялал жуулчлалын 1+1 хөтөлбөр", "icon": "✈️", "duration": "1+1 жил", "type": "Хамтарсан хөтөлбөр", "slug": "tourism-11"},
    {"name": "Хүний нөөцийн менежмент", "icon": "👥", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "hr"},
    {"name": "Тайз дэлгэцийн дизайн технологи", "icon": "🎭", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "stage"},
    {"name": "Вэб дизайн", "icon": "💻", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "web"},
    {"name": "Оёмол бүтээгдэхүүн үйлдвэрлэл", "icon": "🪡", "duration": "1.5 жил", "type": "Техникийн боловсрол", "slug": "sewing"},
    {"name": "Үсчин, гоо сайхан", "icon": "✂️", "duration": "1+1 жил", "type": "Хамтарсан хөтөлбөр", "slug": "hair"},
    {"name": "Аялал жуулчлалын үйлчилгээ", "icon": "🌍", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "tourism"},
    {"name": "Зочид буудал, зоогийн газрын үйлчилгээ", "icon": "🏨", "duration": "3 жил", "type": "Мэргэжлийн боловсрол", "slug": "hotel"}
]

@app.route("/")
def home():
    return render_template("index.html", majors=majors)

@app.route("/taniltsuulga")
def taniltsuulga():
    return render_template("taniltsuulga.html")

@app.route("/mergejil")
def mergejil():
    return render_template("mergejil.html", majors=majors)

@app.route("/mergejil/<slug>")
def mergejil_detail(slug):
    major = next((m for m in majors if m["slug"] == slug), None)
    if major is None:
        abort(404)
    return render_template("mergejil_detail.html", major=major)

@app.route("/hutulbur")
def hutulbur():
    return render_template("hutulbur.html", majors=majors)

@app.route("/elselt")
def elselt():
    return render_template("elselt.html", majors=majors)

@app.route("/bagsh")
def bagsh():
    return render_template("bagsh.html")

@app.route("/medee")
def medee():
    return render_template("medee.html")

@app.route("/zurag")
def zurag():
    return render_template("zurag.html")

@app.route("/holboo")
def holboo():
    return render_template("holboo.html")

if __name__ == "__main__":
    app.run(debug=True)
