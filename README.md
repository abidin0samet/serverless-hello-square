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

---

## 🚀 Kurulum ve Çalıştırma (Local + AWS)

Bu projeyi kendi ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### ✅ Gereksinimler
- AWS hesabı
- AWS CLI kurulu olmalı (`aws configure` yapılmış olmalı)
- AWS SAM CLI kurulu olmalı
- Python 3.10 veya üzeri
- Git

---

### 🔽 1. Depoyu Klonlayın
```bash
git clone https://github.com/<kullanici-adin>/serverless-hello-square.git
cd serverless-hello-square

## Sanal Ortam Oluşturun ve Bağımlılıkları Kurun
python3 -m venv .venv
source .venv/bin/activate  # Windows için: .venv\Scripts\activate
pip install -r requirements.txt

## AWS Kimlik Bilgilerini Tanımlayın
aws configure

##Projeyi Build Edin
sam build

##AWS Üzerine Deploy Edin
sam deploy \
  --stack-name hello-square-stack \
  --resolve-s3 \
  --capabilities CAPABILITY_IAM \
  --region eu-central-1 \
  --confirm-changeset


