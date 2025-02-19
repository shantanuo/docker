FROM ubuntu:latest

# Install LibreOffice and scripting dependencies
RUN apt-get update && apt-get install -y libreoffice libreoffice-script-provider-python libreoffice-script-provider-bsh libreoffice-script-provider-js

# Install required dependencies
RUN apt-get update && apt-get install -y wget unzip fonts-dejavu

# Download and install Shobhika font
RUN mkdir -p /usr/share/fonts/truetype/shobhika && wget -O /tmp/Shobhika.zip https://github.com/Sandhi-IITBombay/Shobhika/releases/download/v1.05/Shobhika-1.05.zip && unzip /tmp/Shobhika.zip -d /tmp/shobhika && mv /tmp/shobhika/Shobhika-1.05/*.otf /usr/share/fonts/truetype/shobhika/ 

# Create necessary directories with proper permissions
RUN mkdir -p /app/.config/libreoffice/4/user/basic/Standard
RUN chmod -R 777 /app/.config

# Set LibreOffice user profile path
ENV UserInstallation=file:///app/.config/libreoffice/4/user

WORKDIR /app
COPY StyleLibrary.oxt /app/
COPY marathi_spell_check.oxt /app/
COPY myfile.txt /app/

RUN unopkg add /app/StyleLibrary.oxt --shared
RUN unopkg add /app/marathi_spell_check.oxt --shared

# Run the LibreOffice macro
CMD soffice --headless --invisible --norestore "macro:///StyleLibrary.Module1.myStyleMacro2(\"/app/myfile.txt\")"
