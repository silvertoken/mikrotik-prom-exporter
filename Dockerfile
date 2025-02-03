FROM python:3-alpine
LABEL org.opencontainers.image.source github.com/silvertoken/mikrotik-prom-exporter
RUN addgroup -S mktpe && adduser -S mktpe -G mktpe

ENV MKTPE_CONFIG="/mktpe/mktpe.conf"
WORKDIR /mktpe
COPY mikrotik_prom_exporter/* requirements.txt /mktpe/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5000

USER mktpe
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "mikrotik-prom-exporter:app"]