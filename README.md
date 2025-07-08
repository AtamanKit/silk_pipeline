silk_pipeline/                   ← project root
├── api_clients/                ← API clients for Qualys & Crowdstrike
│   ├── __init__.py
│   ├── base_client.py
│   ├── qualys_client.py
│   └── crowdstrike_client.py
│
├── models/                     ← Pydantic models (normalized host etc.)
│   ├── __init__.py
│   └── host.py
│
├── normalizers/               ← Vendor-specific normalization
│   ├── __init__.py
│   ├── base_normalizer.py
│   ├── qualys_normalizer.py
│   └── crowdstrike_normalizer.py
│
├── deduplicator/              ← Deduplication logic
│   ├── __init__.py
│   └── deduplicator.py
│
├── db/                        ← MongoDB connection & helpers
│   ├── __init__.py
│   └── mongo.py
│
├── visualizations/            ← Matplotlib or Plotly charts
│   └── generate_charts.py
│
├── main.py                    ← Entry point: orchestrates fetch → normalize → dedupe → store → visualize
├── requirements.txt           ← Python dependencies
├── .env                       ← Your actual environment variables
├── .env.example               ← Template for reviewers (no secrets)
│
├── Dockerfile                 ← Image for the Python app
├── docker-compose.yml         ← Orchestrates app + MongoDB containers
│
├── README.md                  ← Setup & run instructions
└── .gitignore
