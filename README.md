# MARSWALK / MARS GUARD

NASA Space Apps research demonstration: interactive local HiRISE terrain, route planning, exclusions and mission reports. Global terrain and environment scenarios are labelled simulations; named local science pins are provisional.

## Source and deployment

The authenticated upload interface accepts UTF-8 text files. The complete deployment source is therefore stored as a lossless, checksum-verified ZIP split into base64 transport parts under `deployment/`. These are data files, not credentials. Run `python unpack.py` to restore the normal Python, frontend, configuration, tests and provenance source tree under `application/`. Review and edit that restored source to develop the project.

SHA-256 of the compressed source: `8f2ff87d150099730ac7fd83e6fb9832d919e83da355805767ee8ef68bf8dd22`.

The Dockerfile verifies and extracts the archive in a build stage, builds the existing MARS GUARD frontend and starts the Python backend as an unprivileged user. No runtime download from NASA is required. The runtime terrain and public assets are checked at startup against their recorded checksums.

Use one Render Free web service in Singapore, Docker runtime. The port follows Render's PORT variable. Dataset ingestion is disabled by default. Uploaded data would be temporary because the free service has no persistent disk. Mission JSON can be downloaded to the user's computer.

## Verification

The supplied local release passed 73 Python tests, with seven GIS-dependent tests skipped, plus dashboard/adapter tests. A fresh official NASA HiRISE source check matched every one of 2,063,307 native terrain samples. Detailed scope and limitations are included inside `application/RELEASE_STATUS.md` and source provenance.

Live deployment test results will be recorded separately after the service is deployed. This is a research demonstration, not a flight-certified astronaut safety system.
