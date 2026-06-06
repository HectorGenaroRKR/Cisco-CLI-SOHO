# SOHO Network Automation & Hardening (NetDevOps)

Este repositorio contiene la arquitectura de configuración y los scripts de automatización en Python para el despliegue seguro de una infraestructura de red SOHO (Small Office / Home Office) basada en equipos Cisco. 

El proyecto implementa el paradigma de **Infraestructura como Código (IaC)** para gestionar y fortificar tanto el Plano de Datos como el Plano de Control de los dispositivos perimetrales y de distribución.

## 🏗️ Arquitectura y Tecnologías Implementadas

### Router Perimetral (R1)
* **Control Plane Policing (CoPP):** Protección del procesador de ruteo contra ataques de denegación de servicio (DDoS), garantizando ancho de banda exclusivo para el tráfico de gestión (SSH/ICMP).
* **Quality of Service (QoS):** Arquitectura MQC con LLQ (Low Latency Queuing) para priorización de telemetría y *Traffic Shaping* para limitar el tráfico de datos generales (Bulk) a 10 Mbps.
* **Seguridad Perimetral:** Listas de Control de Acceso (ACLs) y NAT con ofuscación de puertos para conexiones SSH externas.

### Switch de Distribución (SW1 - Capa 2)
* **Mitigación de MitM:** Implementación de Dynamic ARP Inspection (DAI) validado contra la base de datos de DHCP Snooping.
* **Hardening de Puertos:** Port Security (Restricción MAC) y BPDU Guard para mitigar topologías Spanning-Tree no autorizadas.
* **Resiliencia Operativa:** Mecanismos de auto-recuperación (Errdisable Recovery) para violaciones de seguridad aisladas.

---

## 📂 Estructura del Proyecto

El repositorio está modularizado separando el motor de ejecución, el inventario y las configuraciones finales:

```text
Cisco-CLI-SOHO/
├── configs/                # Archivos de configuración en texto plano (Payloads)
│   ├── R1.cfg              # Políticas MQC, CoPP y ruteo
│   └── SW1.cfg             # Hardening L2 y DAI
├── auditor_ssh.py          # Script de telemetría y verificación de conexión
├── deploy.py               # Motor de automatización (Push de configuraciones)
├── devices.py              # Inventario y gestión de credenciales (Diccionarios)
├── requirements.txt        # Dependencias del entorno de Python
└── README.md
```
## 🛠️ Compatibilidad
Estas configuraciones están diseñadas con comandos estándar de Cisco IOS y han sido probadas en entornos virtualizados ejecutando versiones **12.4** (como los modelos 3745 y 7200), siendo totalmente compatibles con versiones de IOS 15.x y hardware físico moderno.
