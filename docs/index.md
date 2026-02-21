:yment Service
Bienvenido a la documentación del servicio de pagos.

## Endpoints
* `GET /`: Estado del servicio.
* `POST /pay`: Procesar un nuevo pago.

## Contacto
Para soporte, contactar al equipo de **Fintech Squad**.services:
  backstage:
    # Esta es la imagen oficial del repositorio de demostración de Spotify
    image: ghcr.io/backstage/backstage:latest
    container_name: backstage-lab
    ports:
      - "9051:3000"
    environment:
      - APP_CONFIG_app_baseUrl=http://localhost:9051
      - APP_CONFIG_backend_baseUrl=http://localhost:7007
      - APP_CONFIG_backend_cors_origin=http://localhost:9051

