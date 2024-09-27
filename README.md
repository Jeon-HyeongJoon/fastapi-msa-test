# fastapi-msa-test

fastapi를 사용한 msa 구조 서비스

시작
```bash
docker-compose up
```

구조
```bash
.
├── README.md
├── docker-compose.yml
├── gateway
│   ├── app
│   │   └── gateway.py
│   └── dockerfile
├── order-service
│   ├── app
│   │   └── order_service.py
│   └── dockerfile
├── poetry.lock
├── pyproject.toml
└── user-service
    ├── app
    │   └── user_service.py
    └── dockerfile
```
