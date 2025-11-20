NeuroFold — AI-Powered Protein Stability & Mutation Prediction

NeuroFold is a full-stack scientific platform for predicting protein folding state, PSI (Protein Stability Index), disease-associated mutations, and generating explainable AI visualizations (SHAP).
It delivers a modern UI, optimized bioinformatics backend, and an ML pipeline designed for real scientific workflows.

Features
User-Facing

→ Upload PDB protein structure files
→ Interactive 3D protein viewer (NGL Viewer)
→ Folding state classification
→ PSI stability prediction
→ SHAP-based interpretability
→ Disease mutation mapping
→ Downloadable PDF reports
→ Email notifications
→ Recent analyses dashboard

Backend & ML

→ PDB parsing using BioPython
→ DSSP-based secondary structure extraction
→ Custom feature engineering module
→ Random Forest prediction engine
→ SHAP explanation generation
→ ReportLab-based PDF report builder
→ Celery + Redis background workers

Project Structure
NeuroFold/
│
├── frontend/ # Next.js 14 UI  
├── backend/ # FastAPI API  
├── ml/ # ML models, training, inference  
├── storage/ # Uploaded files, PDF reports, SHAP images  
├── docs/ # Architecture, API specs  
└── tools/ # DSSP, Postgres, Redis setup scripts

Tech Stack
Frontend

→ Next.js 14
→ Tailwind CSS
→ Framer Motion
→ NGL Viewer
→ Nivo Charts

Backend

→ FastAPI
→ SQLAlchemy + Alembic
→ JWT Authentication
→ ReportLab PDF generation
→ SendGrid / SMTP integration

Machine Learning & Bioinformatics

→ Scikit-learn
→ SHAP
→ NumPy / Pandas
→ BioPython
→ DSSP (mkdssp)

Infrastructure

→ PostgreSQL
→ Redis + Celery
→ Docker (optional)
→ Nginx (optional)

How It Works

User uploads a PDB structure file

Backend processes structure and extracts:
→ Secondary structure (DSSP)
→ Sequence & atomic features
→ Physicochemical descriptors

ML pipeline predicts:
→ Folding state
→ PSI stability index
→ SHAP feature contributions
→ Disease-mutation likelihood

Results stored in PostgreSQL

A scientific PDF report is generated

Frontend displays:
→ 3D protein visualization
→ PSI gauges and charts
→ SHAP plots
→ Structural analytics
→ Disease association summaries

Installation (High-Level)
Requirements

→ Node.js 18+
→ Python 3.10+
→ PostgreSQL
→ Redis
→ mkdssp installed locally

Backend Setup
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend Setup
cd frontend
npm install
npm run dev

ML Pipeline
cd ml
python train_model.py

Environment Variables

Backend .env:

DATABASE_URL=postgresql://user:password@localhost:5432/neurofold
SECRET_KEY=your-secret-key
SENDGRID_API_KEY=your-api-key
REDIS_URL=redis://localhost:6379/0

Frontend .env:

NEXT_PUBLIC_API_URL=http://localhost:8000

Roadmap

→ Protein embeddings using ESM2
→ Zero-shot mutation impact prediction
→ Batch analysis support
→ Enhanced PDF report design
→ Public API documentation

License

MIT License.
Open for academic and research use.

Contact

NeuroFold — AI Platform for Protein Stability and Mutation Prediction
Built for bioinformatics learning, research, and protein analysis.
