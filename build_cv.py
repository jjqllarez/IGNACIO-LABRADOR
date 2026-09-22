import base64

with open('foto_ignacio.png', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Currículum Vitae - Ignacio Labrador</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1e3a8a;          /* Azul marino corporativo */
      --primary-dark: #0f172a;     /* Carbón profundo */
      --sidebar-bg: #f1f5f9;       /* Gris clarito elegante y limpio */
      --sidebar-border: #e2e8f0;   /* Borde divisorio sutil */
      --sidebar-text: #0f172a;     /* Texto oscuro para máxima legibilidad */
      --sidebar-muted: #475569;    /* Gris medio */
      --accent: #2563eb;           /* Azul acento profesional */
      --accent-light: #eff6ff;     /* Fondo azul muy suave */
      --main-bg: #ffffff;
      --text-main: #0f172a;
      --text-body: #334155;
      --text-muted: #64748b;
      --border-light: #e2e8f0;
      --card-bg: #f8fafc;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #cbd5e1;
      color: var(--text-body);
      line-height: 1.4;
      font-size: 12px;
      -webkit-font-smoothing: antialiased;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 16px 8px 36px;
    }}

    /* Barra de herramientas superior flotante */
    .toolbar {{
      width: 8.5in;
      max-width: 100%;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #ffffff;
      padding: 10px 18px;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
      border: 1px solid #cbd5e1;
    }}

    .toolbar-info {{
      font-size: 13px;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .toolbar-badge {{
      background: #eff6ff;
      color: #1d4ed8;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 9999px;
      border: 1px solid #bfdbfe;
    }}

    .toolbar-actions {{
      display: flex;
      gap: 10px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 15px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 12.5px;
      cursor: pointer;
      border: none;
      transition: all 0.15s ease;
      text-decoration: none;
    }}

    .btn-print {{
      background-color: #1e3a8a;
      color: #ffffff;
    }}

    .btn-print:hover {{
      background-color: #1d4ed8;
      transform: translateY(-1px);
    }}

    .btn-copy {{
      background-color: #f8fafc;
      color: #0f172a;
      border: 1px solid #cbd5e1;
    }}

    .btn-copy:hover {{
      background-color: #e2e8f0;
    }}

    /* ========================================================
       DOCUMENTO HOJA CARTA EXACTA (8.5in x 11in)
       ======================================================== */
    .cv-page {{
      width: 8.5in;
      height: 11in;
      max-height: 11in;
      background: #ffffff;
      display: grid;
      grid-template-columns: 2.85in 5.65in;
      box-shadow: 0 16px 36px rgba(15, 23, 42, 0.18);
      border-radius: 2px;
      overflow: hidden;
      position: relative;
    }}

    /* ========================================================
       SIDEBAR (GRIS CLARITO EDITORIAL Y PULCRO)
       ======================================================== */
    .cv-sidebar {{
      background-color: var(--sidebar-bg);
      color: var(--sidebar-text);
      padding: 0.44in 0.25in 0.38in 0.28in;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 11in;
      max-height: 11in;
      overflow: hidden;
      border-right: 1px solid var(--sidebar-border);
    }}

    .sidebar-top-group {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* Foto de Perfil circular */
    .photo-wrapper {{
      display: flex;
      justify-content: center;
      margin-bottom: 2px;
    }}

    .photo-circle {{
      width: 130px;
      height: 130px;
      border-radius: 50%;
      border: 4px solid #ffffff;
      box-shadow: 0 6px 16px rgba(15, 23, 42, 0.14);
      object-fit: cover;
      display: block;
      background-color: #ffffff;
    }}

    /* Nombre y Título */
    .sidebar-header {{
      text-align: center;
    }}

    .candidate-name {{
      font-size: 22px;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: 0.5px;
      color: var(--primary-dark);
      text-transform: uppercase;
      margin-bottom: 3px;
    }}

    .candidate-tagline {{
      font-size: 10px;
      font-weight: 700;
      color: var(--accent);
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .sidebar-divider {{
      border: none;
      height: 1px;
      background-color: var(--sidebar-border);
      margin: 1px 0;
    }}

    /* Títulos de sección en sidebar */
    .sidebar-title {{
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: var(--primary);
      margin-bottom: 5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .sidebar-title svg {{
      width: 13px;
      height: 13px;
      stroke: var(--accent);
    }}

    /* Lista de Contacto */
    .contact-list {{
      display: flex;
      flex-direction: column;
      gap: 5.5px;
      font-size: 11px;
      line-height: 1.35;
    }}

    .contact-item {{
      display: flex;
      align-items: flex-start;
      gap: 7px;
      color: var(--text-main);
      text-decoration: none;
    }}

    .contact-icon {{
      width: 13px;
      height: 13px;
      stroke: var(--accent);
      flex-shrink: 0;
      margin-top: 1.5px;
    }}

    .contact-text {{
      display: flex;
      flex-direction: column;
    }}

    .contact-text .label {{
      font-size: 9.5px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      color: var(--sidebar-muted);
      font-weight: 700;
      line-height: 1.1;
    }}

    .contact-text .val {{
      font-size: 11px;
      font-weight: 600;
      color: var(--primary-dark);
    }}

    .contact-text .email-val {{
      font-size: 9.8px;
      letter-spacing: -0.2px;
      color: var(--primary-dark);
      word-break: break-word;
    }}

    /* Card de Disponibilidad en Sidebar */
    .availability-card {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      padding: 6.5px 10px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 7px;
    }}

    .avail-indicator {{
      width: 7px;
      height: 7px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 6px #10b981;
      flex-shrink: 0;
    }}

    .avail-text {{
      font-size: 10px;
      color: #065f46;
      font-weight: 700;
      line-height: 1.25;
    }}

    /* Áreas de Competencia */
    .competency-group {{
      margin-bottom: 5px;
    }}

    .competency-group:last-child {{
      margin-bottom: 0;
    }}

    .competency-name {{
      font-size: 10.5px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1px;
    }}

    .competency-sub {{
      font-size: 9.8px;
      color: var(--sidebar-muted);
      line-height: 1.35;
    }}

    /* Habilidades Blandas (Tags en fondo blanco con sombra sutil) */
    .soft-skills-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }}

    .soft-tag {{
      background: #ffffff;
      color: #1e293b;
      border: 1px solid #cbd5e1;
      padding: 3px 7px;
      border-radius: 4px;
      font-size: 9.8px;
      font-weight: 600;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    }}

    .sidebar-footer {{
      padding-top: 8px;
      border-top: 1px solid var(--sidebar-border);
      font-size: 9.5px;
      color: var(--sidebar-muted);
      text-align: center;
      line-height: 1.35;
      font-weight: 500;
    }}

    /* ========================================================
       COLUMNA PRINCIPAL (EDITORIAL Y MODERNA)
       ======================================================== */
    .cv-main {{
      background-color: #ffffff;
      padding: 0.44in 0.42in 0.38in 0.38in;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 11in;
      max-height: 11in;
      overflow: hidden;
    }}

    .main-top-group {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* Encabezados de sección principal */
    .main-section {{
      display: flex;
      flex-direction: column;
    }}

    .section-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }}

    .section-title {{
      font-size: 12.8px;
      font-weight: 800;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: var(--primary-dark);
      white-space: nowrap;
    }}

    .section-line {{
      flex: 1;
      height: 1.5px;
      background: linear-gradient(to right, #1e3a8a, #e2e8f0);
    }}

    /* Perfil Profesional */
    .profile-card {{
      background-color: var(--card-bg);
      border-left: 3.5px solid var(--primary);
      padding: 9px 13px;
      border-radius: 0 6px 6px 0;
      border-top: 1px solid #f1f5f9;
      border-right: 1px solid #f1f5f9;
      border-bottom: 1px solid #f1f5f9;
    }}

    .profile-card p {{
      font-size: 11px;
      line-height: 1.5;
      color: #334155;
      text-align: justify;
    }}

    /* Lista de Experiencia */
    .experience-list {{
      display: flex;
      flex-direction: column;
      gap: 9.5px;
    }}

    .job-entry {{
      display: flex;
      flex-direction: column;
    }}

    .job-top {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 6px;
    }}

    .job-role {{
      font-size: 11.8px;
      font-weight: 700;
      color: var(--primary-dark);
    }}

    .job-location {{
      font-size: 10.5px;
      color: #64748b;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 3px;
    }}

    .job-company {{
      font-size: 10.8px;
      font-weight: 600;
      color: var(--accent);
      margin-bottom: 2px;
    }}

    .job-bullets {{
      list-style: none;
      padding: 0;
      margin: 2px 0 0 0;
      font-size: 10.5px;
      line-height: 1.38;
      color: #334155;
    }}

    .job-bullets li {{
      position: relative;
      padding-left: 11px;
      margin-bottom: 1.5px;
    }}

    .job-bullets li::before {{
      content: "•";
      position: absolute;
      left: 1px;
      color: var(--accent);
      font-size: 12px;
      top: 0;
    }}

    .job-bullets li strong {{
      color: var(--primary-dark);
    }}

    /* Disponibilidad al pie */
    .dispo-box {{
      background-color: #f0fdf4;
      border: 1px solid #bbf7d0;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 10.8px;
      color: #166534;
      line-height: 1.45;
    }}

    .dispo-box strong {{
      color: #14532d;
    }}

    /* Toast */
    #toast {{
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(80px);
      background: #0f172a;
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      transition: transform 0.25s ease;
      z-index: 999;
      pointer-events: none;
    }}

    #toast.show {{
      transform: translateX(-50%) translateY(0);
    }}

    /* ========================================================
       REGLAS ESTRICTAS PARA IMPRESIÓN (1 SOLA PÁGINA CARTA)
       ======================================================== */
    @page {{
      size: letter portrait;
      margin: 0;
    }}

    @media print {{
      html, body {{
        width: 8.5in !important;
        height: 11in !important;
        max-height: 11in !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        overflow: hidden !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}

      .toolbar, #toast {{
        display: none !important;
      }}

      .cv-page {{
        width: 8.5in !important;
        height: 11in !important;
        max-height: 11in !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
      }}

      .cv-sidebar {{
        background-color: #f1f5f9 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Barra de Herramientas Superior -->
  <div class="toolbar">
    <div class="toolbar-info">
      <span class="toolbar-badge">1 Hoja Carta Exacta</span>
      <span>Currículum Vitae &bull; Ignacio Labrador</span>
    </div>
    <div class="toolbar-actions">
      <button class="btn btn-copy" onclick="copiarContacto()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        Copiar Contacto
      </button>
      <button class="btn btn-print" onclick="window.print()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        Imprimir / Guardar en PDF
      </button>
    </div>
  </div>

  <!-- DOCUMENTO EN 1 HOJA CARTA -->
  <div class="cv-page">

    <!-- COLUMNA LATERAL (GRIS CLARITO EDITORIAL) -->
    <aside class="cv-sidebar">

      <div class="sidebar-top-group">
        <!-- FOTO EXTRAÍDA CON MARCO BLANCO ELEGANTE -->
        <div class="photo-wrapper">
          <img class="photo-circle" src="data:image/png;base64,{photo_b64}" alt="Foto de Ignacio Labrador">
        </div>

        <!-- NOMBRE Y TÍTULO -->
        <div class="sidebar-header">
          <h1 class="candidate-name">IGNACIO<br>LABRADOR</h1>
          <div class="candidate-tagline">Operaciones &bull; Servicios &bull; Mantenimiento</div>
        </div>

        <hr class="sidebar-divider">

        <!-- CONTACTO -->
        <div>
          <div class="sidebar-title">
            <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            CONTACTO
          </div>
          <div class="contact-list">
            <a class="contact-item" href="tel:04221110096">
              <svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <div class="contact-text">
                <span class="label">Teléfono</span>
                <span class="val">0422-1110096</span>
              </div>
            </a>
            <a class="contact-item" href="mailto:ignacio.labrador.rodriguez@gmail.com">
              <svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <div class="contact-text">
                <span class="label">Correo Electrónico</span>
                <span class="val email-val">ignacio.labrador.rodriguez@gmail.com</span>
              </div>
            </a>
            <div class="contact-item">
              <svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><line x1="15" y1="8" x2="17" y2="8"></line><line x1="15" y1="12" x2="17" y2="12"></line><line x1="7" y1="16" x2="17" y2="16"></line></svg>
              <div class="contact-text">
                <span class="label">Documento de Identidad</span>
                <span class="val">C.I.: 29.698.769</span>
              </div>
            </div>
          </div>
        </div>

        <!-- BADGE DISPONIBILIDAD -->
        <div class="availability-card">
          <span class="avail-indicator"></span>
          <span class="avail-text">Disponibilidad Inmediata &bull; Flexibilidad Total</span>
        </div>

        <hr class="sidebar-divider">

        <!-- COMPETENCIAS Y ÁREAS CLAVE -->
        <div>
          <div class="sidebar-title">
            <svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            ÁREAS DE EXPERIENCIA
          </div>

          <div class="competency-group">
            <div class="competency-name">Atención al Cliente y Ventas</div>
            <div class="competency-sub">Atención personalizada &bull; Mesero &bull; Ventas y perifoneo</div>
          </div>

          <div class="competency-group">
            <div class="competency-name">Administración y Logística</div>
            <div class="competency-sub">Asistencia administrativa &bull; Control de inventarios &bull; Almacén</div>
          </div>

          <div class="competency-group">
            <div class="competency-name">Mantenimiento y Construcción</div>
            <div class="competency-sub">Albañilería (empañetado, estucado, enchapado) &bull; Pintura</div>
          </div>

          <div class="competency-group">
            <div class="competency-name">Seguridad e Infraestructura</div>
            <div class="competency-sub">Mantenimiento de piscinas y fincas &bull; Monitoreo CCTV</div>
          </div>

          <div class="competency-group">
            <div class="competency-name">Creatividad y Detalles</div>
            <div class="competency-sub">Confección de detalles &bull; Auxiliar florista &bull; Bartender</div>
          </div>
        </div>

        <hr class="sidebar-divider">

        <!-- HABILIDADES BLANDAS -->
        <div>
          <div class="sidebar-title">
            <svg viewBox="0 0 24 24" fill="none" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            HABILIDADES BLANDAS
          </div>
          <div class="soft-skills-tags">
            <span class="soft-tag">Adaptabilidad</span>
            <span class="soft-tag">Comunicación asertiva</span>
            <span class="soft-tag">Proactividad</span>
            <span class="soft-tag">Trabajo bajo presión</span>
            <span class="soft-tag">Organización</span>
            <span class="soft-tag">Resolución de problemas</span>
            <span class="soft-tag">Trabajo en equipo</span>
          </div>
        </div>
      </div>

      <!-- FOOTER SIDEBAR -->
      <div class="sidebar-footer">
        Residencia: Venezuela &bull; Referencias comprobables a solicitud
      </div>

    </aside>

    <!-- COLUMNA PRINCIPAL (BLANCA / EDITORIAL) -->
    <main class="cv-main">

      <div class="main-top-group">
        <!-- PERFIL PROFESIONAL -->
        <section class="main-section">
          <div class="section-header">
            <h2 class="section-title">PERFIL PROFESIONAL</h2>
            <div class="section-line"></div>
          </div>
          <div class="profile-card">
            <p>
              Profesional versátil y proactivo con sólida experiencia en atención al cliente, gestión operativa y mantenimiento general de infraestructura. Destaca por su alta capacidad de adaptación, rigurosa atención al detalle y destreza en la ejecución simultánea de múltiples funciones con orden y pulcritud. Orientado a resultados, con habilidades comprobadas para el trabajo colaborativo, la resolución eficiente de problemas y la preservación de estándares óptimos en diversos entornos laborales.
            </p>
          </div>
        </section>

        <!-- EXPERIENCIA LABORAL -->
        <section class="main-section">
          <div class="section-header">
            <h2 class="section-title">EXPERIENCIA LABORAL</h2>
            <div class="section-line"></div>
          </div>

          <div class="experience-list">

            <!-- 1. Trabajos Independientes -->
            <article class="job-entry">
              <div class="job-top">
                <span class="job-role">Especialista en Oficios Generales e Infraestructura</span>
                <span class="job-location">Servicios Técnicos Independientes</span>
              </div>
              <div class="job-company">Trabajador Independiente</div>
              <ul class="job-bullets">
                <li><strong>Albañilería y Acabados:</strong> Ejecución técnica de empañetado, estucado fino y enchapado cerámico con óptima terminación.</li>
                <li><strong>Mantenimiento de Instalaciones:</strong> Pintura de estructuras residenciales y comerciales; balance químico y tratamiento de piscinas.</li>
                <li><strong>Conservación y Seguridad:</strong> Mantenimiento de áreas verdes en fincas y operación técnica de sistemas de videovigilancia CCTV.</li>
              </ul>
            </article>

            <!-- 2. Bodegón Carpio -->
            <article class="job-entry">
              <div class="job-top">
                <span class="job-role">Asistente Administrativo, Bartender y Mesero</span>
                <span class="job-location">El Tigre, Anzoátegui</span>
              </div>
              <div class="job-company">Bodegón Carpio</div>
              <ul class="job-bullets">
                <li>Gestión administrativa integral de piso, apoyo en cuadre de caja, supervisión de inventario y reposición de mercancía.</li>
                <li>Servicio de coctelería y atención cordial de alto estándar a comensales en barra y mesa.</li>
              </ul>
            </article>

            <!-- 3. Tropas Sport's -->
            <article class="job-entry">
              <div class="job-top">
                <span class="job-role">Atención al Público y Asesor de Ventas</span>
                <span class="job-location">El Tigre, Anzoátegui</span>
              </div>
              <div class="job-company">Tropas Sport's</div>
              <ul class="job-bullets">
                <li>Asesoría comercial directa y personalizada sobre productos deportivos, garantizando una excelente experiencia de compra y control de piso.</li>
              </ul>
            </article>

            <!-- 4. Atípico Café & Bar -->
            <article class="job-entry">
              <div class="job-top">
                <span class="job-role">Atención al Cliente y Mesero</span>
                <span class="job-location">Barinas, Barinitas</span>
              </div>
              <div class="job-company">Atípico Café & Bar</div>
              <ul class="job-bullets">
                <li>Servicio dinámico de atención a mesas, manteniendo altos estándares de hospitalidad, pulcritud, rapidez y cortesía.</li>
              </ul>
            </article>

            <!-- 5. Inversiones Maralfri -->
            <article class="job-entry">
              <div class="job-top">
                <span class="job-role">Almacenista, Perifoneador y Atención al Cliente</span>
                <span class="job-location">Valencia, Tinaquillo</span>
              </div>
              <div class="job-company">Inversiones Maralfri</div>
              <ul class="job-bullets">
                <li>Control físico de inventarios, gestión de almacén y promoción de productos mediante perifoneo comercial dinámico.</li>
              </ul>
            </article>

            <!-- 6. Floristería María José -->
            <article class="job-entry">
              <div class="job-top">
                <span class="job-role">Auxiliar Florista, Creador de Detalles y Atención</span>
                <span class="job-location">Acacías, Meta, Colombia</span>
              </div>
              <div class="job-company">Floristería María José</div>
              <ul class="job-bullets">
                <li>Confección de arreglos florales, diseño de detalles creativos personalizados y atención orientada a la fidelización del público.</li>
              </ul>
            </article>

          </div>
        </section>
      </div>

      <!-- DISPONIBILIDAD -->
      <section class="main-section">
        <div class="section-header">
          <h2 class="section-title">DISPONIBILIDAD LABORAL</h2>
          <div class="section-line"></div>
        </div>
        <div class="dispo-box">
          <strong>Incorporación inmediata:</strong> Total flexibilidad horaria para desempeñar funciones en turnos diurnos, nocturnos o rotativos según los requerimientos operativos de la empresa.
        </div>
      </section>

    </main>

  </div>

  <div id="toast">Datos de contacto copiados al portapapeles</div>

  <script>
    function copiarContacto() {{
      const texto = "IGNACIO LABRADOR\\nTeléfono: 0422-1110096\\nEmail: ignacio.labrador.rodriguez@gmail.com\\nC.I.: 29.698.769";
      navigator.clipboard.writeText(texto).then(() => {{
        const toast = document.getElementById('toast');
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2500);
      }}).catch(() => {{
        alert(texto);
      }});
    }}
  </script>

</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated light-gray index.html successfully!')
