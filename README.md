# serverless-hello-square
# Serverless API – AWS Lambda + API Gateway (My First Serverless Function+)

AWS Lambda ve Amazon API Gateway kullanılarak geliştirilmiş ölçeklenebilir ve yönetilebilir bir **Serverless API** uygulamasıdır. Uygulama, sunucu yönetimi gerektirmeden çalışır ve tamamen AWS üzerinde barınır. Proje Python ile geliştirilmiş ve **AWS SAM (Serverless Application Model)** kullanılarak deploy edilmiştir.

---

## 🧩 Mimari Diyagram


Bu mimaride API Gateway HTTP isteklerini karşılar, Lambda fonksiyonunu tetikler ve tüm kayıtlar CloudWatch üzerinde loglanır.

---

## 🔧 Teknik Bilgiler

| Özellik | Detay |
|---------|-------|
| Programlama Dili | Python 3.11 |
| Mimarî | Serverless |
| AWS Servisleri | Lambda, API Gateway, CloudWatch |
| Framework | AWS SAM |
| Dağıtım (Deploy) | `sam deploy` |
| Loglama | AWS CloudWatch |
| Yetkilendirme | IAM Role (Least Privilege) |

---

## 🌐 API Bilgileri

https://6jzrfifk5l.execute-api.eu-central-1.amazonaws.com   
<img width="1470" height="956" alt="Ekran Resmi 2025-10-22 14 30 11" src="https://github.com/user-attachments/assets/454f71ec-69e4-4986-b2cd-078aad69ac76" />

<img width="1470" height="956" alt="Ekran Resmi 2025-10-22 14 29 54" src="https://github.com/user-attachments/assets/f85a79c4-e908-428d-84ae-24f8b8571e03" />

