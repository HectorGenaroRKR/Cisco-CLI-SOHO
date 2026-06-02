# Plantillas Base de Red SOHO (Cisco IOS)

Este repositorio contiene plantillas de configuración estandarizadas, diseñadas para inicializar y desplegar rápidamente una infraestructura de red SOHO (Small Office / Home Office) utilizando la CLI de Cisco IOS. 

El objetivo de este proyecto es establecer una conectividad base robusta, integrar servicios de red esenciales y aplicar las mejores prácticas de endurecimiento (hardening) de seguridad desde el minuto cero del despliegue.

## 🏗️ Arquitectura y Topología Lógica

El diseño lógico se basa en dos nodos principales:
* **Router (Gateway Perimetral):** Actúa como puerta de enlace, servidor DHCP para la red local, firewall básico de traducción de direcciones (NAT/PAT) y punto de acceso remoto seguro.
* **Switch (Capa de Acceso):** Provee conectividad de Capa 2 para los dispositivos finales (End-Devices), utilizando puertos troncales estáticos hacia el router y una VLAN de administración dedicada.

## ⚙️ Tecnologías y Protocolos Implementados

* **Seguridad y Gestión (Capa de Aplicación):**
  * Acceso remoto cifrado mediante **SSHv2** (módulo RSA de 2048 bits).
  * Cifrado de contraseñas en texto plano y usuarios locales con privilegios administrativos (Nivel 15).
  * Desactivación de búsquedas DNS inadvertidas (`no ip domain-lookup`).
* **Servicios de Red (Capa de Red / Transporte):**
  * **DHCP** configurado con exclusión de IPs estáticas para servidores/gateway.
  * **NAT con sobrecarga (PAT)** vinculado a listas de control de acceso (ACLs) estándar para salida a Internet.
* **Conmutación (Capa de Enlace de Datos):**
  * Puertos **Trunk 802.1Q** estáticos (negociación DTP deshabilitada por seguridad).
  * Interfaz Virtual de Switch (SVI) para administración en banda.
  * **Spanning-Tree PortFast** habilitado en los puertos perimetrales para una transición inmediata al estado de reenvío.

## 🚀 Instrucciones de Despliegue

1. **Obtener las plantillas:** Clona este repositorio o descarga directamente los archivos `R1.cfg` y `SW1.cfg`.
2. **Asignación de Variables:** Abre las plantillas en cualquier editor de código o texto plano. Reemplaza todas las variables encerradas en corchetes angulares `< >` con los parámetros técnicos de tu red. 
   * *Ejemplo:* Modificar `<LAN_IP>` por `192.168.10.1`.
3. **Inyección en la CLI:** 
   * Conéctate al puerto de consola del equipo Cisco (físico) o abre la terminal de tu entorno virtualizado (GNS3, EVE-NG, Packet Tracer).
   * Accede al modo de configuración global (`configure terminal`).
   * Copia y pega los bloques de configuración estructurados.

## 🛠️ Compatibilidad
Estas plantillas están diseñadas con comandos estándar de Cisco IOS y han sido probadas en entornos virtualizados ejecutando versiones **12.4** (como los modelos 3745 y 7200), siendo totalmente compatibles con versiones de IOS 15.x y hardware físico moderno.
