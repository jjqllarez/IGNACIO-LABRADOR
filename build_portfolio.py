import base64

with open('foto_ignacio.png', 'rb') as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ignacio Labrador | Perfil Profesional y Portafolio</title>
  <meta name="description" content="Perfil profesional y portafolio de Ignacio Labrador. Especialista en gestión operativa, atención al cliente de alto nivel y mantenimiento integral. Descarga su currículum o contáctalo directamente por WhatsApp.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #0f172a;
      --primary-light: #1e293b;
      --accent: #2563eb;
      --accent-hover: #1d4ed8;
      --accent-soft: #eff6ff;
      --whatsapp: #22c55e;
      --whatsapp-hover: #16a34a;
      --whatsapp-bg: #ecfdf5;
      --text-main: #0f172a;
      --text-body: #334155;
      --text-muted: #64748b;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --border-color: #e2e8f0;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 14px -2px rgba(15, 23, 42, 0.08);
      --shadow-lg: 0 12px 28px -4px rgba(15, 23, 42, 0.12);
      --radius: 14px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-body);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    /* ========================================================
       BARRA DE NAVEGACIÓN SUPERIOR
       ======================================================== */
    .navbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      padding: 12px 24px;
      transition: all 0.2s ease;
    }}

    .nav-container {{
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text-main);
      font-weight: 800;
      font-size: 17px;
      letter-spacing: -0.3px;
    }}

    .nav-avatar {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      border: 2px solid var(--accent);
      object-fit: cover;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 20px;
      list-style: none;
    }}

    .nav-links a {{
      text-decoration: none;
      color: var(--text-body);
      font-weight: 600;
      font-size: 14px;
      transition: color 0.15s ease;
    }}

    .nav-links a:hover {{
      color: var(--accent);
    }}

    .nav-btn-cv {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: var(--primary);
      color: #ffffff !important;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px !important;
      font-weight: 700;
      transition: all 0.2s ease;
    }}

    .nav-btn-cv:hover {{
      background-color: var(--accent);
      transform: translateY(-1px);
    }}

    /* ========================================================
       HERO SECTION (PRESENTACIÓN PRINCIPAL)
       ======================================================== */
    .hero-section {{
      padding: 60px 20px 50px;
      background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%);
      border-bottom: 1px solid var(--border-color);
    }}

    .hero-container {{
      max-width: 1050px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: auto 1fr;
      gap: 40px;
      align-items: center;
    }}

    .hero-photo-box {{
      position: relative;
      display: flex;
      justify-content: center;
    }}

    .hero-photo {{
      width: 190px;
      height: 190px;
      border-radius: 50%;
      border: 5px solid #ffffff;
      box-shadow: var(--shadow-lg);
      object-fit: cover;
      background-color: #ffffff;
    }}

    .status-badge {{
      position: absolute;
      bottom: 8px;
      background: #ffffff;
      border: 1px solid #bbf7d0;
      box-shadow: var(--shadow-sm);
      color: #15803d;
      padding: 5px 12px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }}

    .status-dot {{
      width: 8px;
      height: 8px;
      background: #22c55e;
      border-radius: 50%;
      animation: pulse 1.8s infinite;
    }}

    @keyframes pulse {{
      0% {{ box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.6); }}
      70% {{ box-shadow: 0 0 0 8px rgba(34, 197, 94, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }}
    }}

    .hero-content h1 {{
      font-size: 38px;
      font-weight: 800;
      color: var(--primary);
      letter-spacing: -0.8px;
      line-height: 1.15;
      margin-bottom: 10px;
    }}

    .hero-subtitle {{
      font-size: 18px;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 14px;
    }}

    .hero-desc {{
      font-size: 15.5px;
      color: var(--text-body);
      max-width: 620px;
      line-height: 1.6;
      margin-bottom: 24px;
    }}

    /* Botones de Acción Hero */
    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .btn-main {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 12px 22px;
      border-radius: 10px;
      font-size: 14.5px;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      border: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .btn-whatsapp {{
      background-color: var(--whatsapp);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3);
    }}

    .btn-whatsapp:hover {{
      background-color: var(--whatsapp-hover);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(34, 197, 94, 0.4);
    }}

    .btn-pdf {{
      background-color: var(--primary);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
    }}

    .btn-pdf:hover {{
      background-color: var(--accent);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
    }}

    .btn-vercel {{
      background-color: #0f172a;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
    }}

    .btn-vercel:hover {{
      background-color: #1e293b;
      transform: translateY(-2px);
    }}

    .btn-outline {{
      background-color: #ffffff;
      color: var(--text-main);
      border: 1.5px solid var(--border-color);
    }}

    .btn-outline:hover {{
      background-color: #f1f5f9;
      border-color: #cbd5e1;
      transform: translateY(-2px);
    }}

    /* ========================================================
       SECCIONES GENERALES
       ======================================================== */
    .section-wrap {{
      max-width: 1050px;
      margin: 0 auto;
      padding: 60px 20px;
    }}

    .section-header-center {{
      text-align: center;
      margin-bottom: 40px;
    }}

    .section-tag {{
      display: inline-block;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--accent);
      background: var(--accent-soft);
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 8px;
    }}

    .section-title-large {{
      font-size: 28px;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.5px;
    }}

    /* ========================================================
       GRID DE SERVICIOS / ESPECIALIDADES
       ======================================================== */
    .services-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
    }}

    .service-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
    }}

    .service-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }}

    .service-icon {{
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: var(--accent-soft);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;
      color: var(--accent);
    }}

    .service-title {{
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 10px;
    }}

    .service-list {{
      list-style: none;
      font-size: 13.5px;
      color: var(--text-body);
      line-height: 1.6;
    }}

    .service-list li {{
      position: relative;
      padding-left: 16px;
      margin-bottom: 6px;
    }}

    .service-list li::before {{
      content: "•";
      position: absolute;
      left: 0;
      color: var(--accent);
      font-weight: bold;
    }}

    /* ========================================================
       SECCIÓN DE CURRÍCULUM DESTACADO (VISOR / ACCIÓN)
       ======================================================== */
    .cv-banner {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      border-radius: 20px;
      padding: 40px 36px;
      box-shadow: var(--shadow-lg);
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 30px;
      align-items: center;
      margin: 20px auto 40px;
    }}

    .cv-banner-content h3 {{
      font-size: 26px;
      font-weight: 800;
      margin-bottom: 8px;
      color: #ffffff;
    }}

    .cv-banner-content p {{
      font-size: 15px;
      color: #cbd5e1;
      max-width: 580px;
      line-height: 1.55;
    }}

    .cv-banner-actions {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .cv-banner-btn-pdf {{
      background-color: var(--accent);
      color: #ffffff;
      padding: 13px 24px;
      border-radius: 10px;
      font-size: 14.5px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
      transition: all 0.2s ease;
    }}

    .cv-banner-btn-pdf:hover {{
      background-color: #3b82f6;
      transform: translateY(-2px);
    }}

    .cv-banner-btn-view {{
      background-color: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 12px 24px;
      border-radius: 10px;
      font-size: 14.5px;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .cv-banner-btn-view:hover {{
      background-color: rgba(255, 255, 255, 0.2);
    }}

    /* ========================================================
       TRAYECTORIA Y EXPERIENCIA
       ======================================================== */
    .timeline-container {{
      max-width: 820px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .timeline-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px 24px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .timeline-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .timeline-role {{
      font-size: 16px;
      font-weight: 800;
      color: var(--primary);
    }}

    .timeline-company {{
      font-size: 14px;
      font-weight: 700;
      color: var(--accent);
    }}

    .timeline-location {{
      font-size: 12.5px;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .timeline-desc {{
      font-size: 13.5px;
      color: var(--text-body);
      line-height: 1.5;
    }}

    /* ========================================================
       SECCIÓN DE CONTACTO
       ======================================================== */
    .contact-grid-boxes {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 18px;
      max-width: 1050px;
      margin: 0 auto;
    }}

    .contact-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 24px 18px;
      text-align: center;
      text-decoration: none;
      color: inherit;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .contact-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: var(--accent);
    }}

    .contact-card-icon {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--accent-soft);
      color: var(--accent);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
    }}

    .contact-card.whatsapp-card .contact-card-icon {{
      background: var(--whatsapp-bg);
      color: var(--whatsapp);
    }}

    .contact-card.web-card .contact-card-icon {{
      background: #f1f5f9;
      color: #0f172a;
    }}

    .contact-card-label {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}

    .contact-card-val {{
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-main);
      word-break: break-word;
    }}

    /* ========================================================
       FOOTER
       ======================================================== */
    footer {{
      background-color: #ffffff;
      border-top: 1px solid var(--border-color);
      padding: 28px 20px;
      text-align: center;
      font-size: 13px;
      color: var(--text-muted);
    }}

    /* ========================================================
       BOTÓN FLOTANTE DE WHATSAPP
       ======================================================== */
    .floating-whatsapp {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999;
      background-color: var(--whatsapp);
      color: #ffffff;
      width: 58px;
      height: 58px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 6px 20px rgba(34, 197, 94, 0.45);
      text-decoration: none;
      transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    .floating-whatsapp:hover {{
      transform: scale(1.08);
      background-color: var(--whatsapp-hover);
      box-shadow: 0 8px 24px rgba(34, 197, 94, 0.55);
    }}

    .floating-whatsapp svg {{
      width: 32px;
      height: 32px;
      fill: currentColor;
    }}

    .whatsapp-tooltip {{
      position: absolute;
      right: 70px;
      background: #0f172a;
      color: #ffffff;
      font-size: 12.5px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 8px;
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      transform: translateX(10px);
      transition: all 0.2s ease;
      box-shadow: var(--shadow-md);
    }}

    .floating-whatsapp:hover .whatsapp-tooltip {{
      opacity: 1;
      transform: translateX(0);
    }}

    /* ========================================================
       MODAL DE VISOR DE CURRÍCULUM
       ======================================================== */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(4px);
      z-index: 1000;
      display: none;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }}

    .modal-overlay.open {{
      display: flex;
    }}

    .modal-card {{
      background: #ffffff;
      width: 100%;
      max-width: 900px;
      height: 90vh;
      border-radius: 16px;
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 20px;
      border-bottom: 1px solid var(--border-color);
      background: #f8fafc;
    }}

    .modal-title {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
    }}

    .modal-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .modal-btn {{
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      border: none;
    }}

    .modal-btn-download {{
      background-color: var(--accent);
      color: #ffffff;
    }}

    .modal-btn-close {{
      background: #e2e8f0;
      color: var(--text-main);
      padding: 6px 12px;
      font-size: 15px;
    }}

    .modal-body {{
      flex: 1;
      overflow: auto;
      padding: 0;
      background: #cbd5e1;
    }}

    .modal-iframe {{
      width: 100%;
      height: 100%;
      border: none;
    }}

    /* Adaptabilidad Móvil */
    @media (max-width: 768px) {{
      .hero-container {{
        grid-template-columns: 1fr;
        text-align: center;
        gap: 24px;
      }}

      .hero-photo-box {{
        margin-bottom: 10px;
      }}

      .hero-content h1 {{
        font-size: 30px;
      }}

      .hero-subtitle {{
        font-size: 16px;
      }}

      .hero-actions {{
        justify-content: center;
      }}

      .cv-banner {{
        grid-template-columns: 1fr;
        text-align: center;
        padding: 30px 20px;
      }}

      .cv-banner-actions {{
        flex-direction: column;
        width: 100%;
      }}

      .nav-links {{
        display: none;
      }}
    }}
  </style>
</head>
<body>

  <!-- Barra de Navegación -->
  <nav class="navbar">
    <div class="nav-container">
      <a href="#" class="nav-brand">
        <img class="nav-avatar" src="data:image/png;base64,{photo_b64}" alt="Ignacio Labrador">
        <span>Ignacio Labrador</span>
      </a>
      <ul class="nav-links">
        <li><a href="#sobre-mi">Sobre Mí</a></li>
        <li><a href="#servicios">Especialidades</a></li>
        <li><a href="#experiencia">Trayectoria</a></li>
        <li><a href="https://ignacio-labrador.vercel.app/" target="_blank" rel="noopener noreferrer">Portafolio Vercel</a></li>
        <li><a href="#contacto">Contacto</a></li>
        <li>
          <a href="curriculum_ignacio_labrador.pdf" download class="nav-btn-cv">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            Descargar CV PDF
          </a>
        </li>
      </ul>
    </div>
  </nav>

  <!-- Hero Section (Presentación) -->
  <section class="hero-section">
    <div class="hero-container">
      
      <!-- Foto de Perfil -->
      <div class="hero-photo-box">
        <img class="hero-photo" src="data:image/png;base64,{photo_b64}" alt="Foto de Ignacio Labrador">
        <div class="status-badge">
          <span class="status-dot"></span>
          Disponible para laborar
        </div>
      </div>

      <!-- Texto Principal -->
      <div class="hero-content">
        <h1>Ignacio Labrador</h1>
        <div class="hero-subtitle">Operaciones &bull; Servicios &bull; Mantenimiento Integral</div>
        <p class="hero-desc">
          Profesional versátil y proactivo con sólida experiencia en atención al cliente personalizada, gestión operativa de inventarios y mantenimiento técnico de instalaciones. Orientado a la eficiencia, el trabajo colaborativo y la excelencia organizativa.
        </p>

        <!-- Botones de Acción -->
        <div class="hero-actions">
          <!-- Botón de WhatsApp -->
          <a class="btn-main btn-whatsapp" href="https://wa.me/584221110096?text=Hola%20Ignacio,%20vi%20tu%20perfil%20web%20y%20me%20gustar%C3%ADa%20conversar%20contigo." target="_blank" rel="noopener noreferrer">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            Contactar por WhatsApp
          </a>

          <!-- Botón de Descargar PDF -->
          <a class="btn-main btn-pdf" href="curriculum_ignacio_labrador.pdf" download="Curriculum_Ignacio_Labrador.pdf">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            Descargar Currículum (PDF)
          </a>

          <!-- Botón a Vercel -->
          <a class="btn-main btn-vercel" href="https://ignacio-labrador.vercel.app/" target="_blank" rel="noopener noreferrer">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            Portafolio Web (Vercel)
          </a>

          <!-- Botón de Ver Currículum Interactivo -->
          <button class="btn-main btn-outline" onclick="abrirModalCV()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
            Ver CV en Pantalla
          </button>
        </div>

      </div>

    </div>
  </section>

  <!-- Banner Destacado de Descarga del CV Oficial -->
  <section class="section-wrap" style="padding-top: 30px; padding-bottom: 20px;">
    <div class="cv-banner">
      <div class="cv-banner-content">
        <h3>¿Necesitas su Currículum Vitae Oficial?</h3>
        <p>
          Documento formal calibrado en <strong>1 sola página tamaño Carta</strong>, perfecto para procesos de selección empresarial, postulaciones operativas y archivo físico o digital.
        </p>
      </div>
      <div class="cv-banner-actions">
        <a class="cv-banner-btn-pdf" href="curriculum_ignacio_labrador.pdf" download="Curriculum_Ignacio_Labrador.pdf">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Descargar PDF Oficial
        </a>
        <button class="cv-banner-btn-view" onclick="abrirModalCV()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          Previsualizar / Imprimir
        </button>
      </div>
    </div>
  </section>

  <!-- Sección: Sobre Mí -->
  <section id="sobre-mi" class="section-wrap" style="padding-top: 10px;">
    <div class="section-header-center">
      <span class="section-tag">Perfil</span>
      <h2 class="section-title-large">Sobre Ignacio Labrador</h2>
    </div>
    <div style="max-width: 820px; margin: 0 auto; background: #ffffff; padding: 30px; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); font-size: 15px; line-height: 1.7; color: var(--text-body);">
      <p style="margin-bottom: 14px;">
        Profesional versátil y proactivo con sólida experiencia en atención al cliente personalizada, gestión operativa de inventarios y mantenimiento integral de instalaciones residenciales y comerciales.
      </p>
      <p style="margin-bottom: 14px;">
        Destaca por su <strong>alta capacidad de adaptación</strong> ante nuevos entornos, rigurosa atención al detalle y destreza técnica para desempeñar múltiples funciones con orden, disciplina y pulcritud.
      </p>
      <p>
        Orientado a resultados tangibles, con excelentes relaciones interpersonales, capacidad demostrada para el trabajo en equipo bajo presión y total disposición para integrarse de inmediato a nuevos retos laborales.
      </p>
    </div>
  </section>

  <!-- Sección: Especialidades y Servicios -->
  <section id="servicios" class="section-wrap" style="background-color: #f1f5f9; max-width: 100%; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
    <div style="max-width: 1050px; margin: 0 auto;">
      <div class="section-header-center">
        <span class="section-tag">Competencias</span>
        <h2 class="section-title-large">Áreas de Especialidad</h2>
      </div>

      <div class="services-grid">
        <!-- 1. Mantenimiento -->
        <div class="service-card">
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>
          </div>
          <h3 class="service-title">Mantenimiento y Obras</h3>
          <ul class="service-list">
            <li>Albañilería de terminación (empañetado, estucado, enchapado).</li>
            <li>Pintura arquitectónica de instalaciones interiores y exteriores.</li>
            <li>Tratamiento químico, filtrado y aspirado de piscinas.</li>
            <li>Conservación y mantenimiento integral de fincas.</li>
          </ul>
        </div>

        <!-- 2. Logística y Almacén -->
        <div class="service-card">
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
          </div>
          <h3 class="service-title">Logística y Almacén</h3>
          <ul class="service-list">
            <li>Gestión y control físico de inventarios y stock.</li>
            <li>Clasificación, estibado seguro y despacho de mercancía.</li>
            <li>Control de piso de venta y reposición oportuna.</li>
            <li>Asistencia administrativa y apoyo en caja.</li>
          </ul>
        </div>

        <!-- 3. Atención al Cliente -->
        <div class="service-card">
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          </div>
          <h3 class="service-title">Atención y Ventas</h3>
          <ul class="service-list">
            <li>Protocolo de hospitalidad y atención personalizada.</li>
            <li>Asesoría comercial directa y cierre de ventas.</li>
            <li>Servicio de barra (Bartender) y mesero en salón.</li>
            <li>Locución comercial y perifoneo dinámico.</li>
          </ul>
        </div>

        <!-- 4. Seguridad y Creatividad -->
        <div class="service-card">
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          </div>
          <h3 class="service-title">Seguridad y Detalles</h3>
          <ul class="service-list">
            <li>Operación técnica y monitoreo preventivo de sistemas CCTV.</li>
            <li>Confección de arreglos florales y detalles manuales personalizados.</li>
            <li>Cuidado y preservación estética de insumos delicados.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Sección: Trayectoria Laboral -->
  <section id="experiencia" class="section-wrap">
    <div class="section-header-center">
      <span class="section-tag">Historial</span>
      <h2 class="section-title-large">Trayectoria Laboral</h2>
    </div>

    <div class="timeline-container">
      
      <div class="timeline-card">
        <div class="timeline-header">
          <span class="timeline-role">Especialista en Oficios Generales e Infraestructura</span>
          <span class="timeline-location">Servicios Técnicos Independientes</span>
        </div>
        <div class="timeline-company">Trabajador Independiente</div>
        <p class="timeline-desc">
          Ejecución autónoma de obras técnicas de albañilería (empañetado, estucado, enchapado cerámico), pintura de instalaciones, balance químico y mantenimiento de piscinas, cuidado de fincas y operación de videovigilancia CCTV.
        </p>
      </div>

      <div class="timeline-card">
        <div class="timeline-header">
          <span class="timeline-role">Asistente Administrativo, Bartender y Mesero</span>
          <span class="timeline-location">El Tigre, Anzoátegui</span>
        </div>
        <div class="timeline-company">Bodegón Carpio</div>
        <p class="timeline-desc">
          Gestión administrativa integral de piso, apoyo en cuadre de caja, supervisión de inventario y reposición de mercancía. Servicio de coctelería y atención protocolar a comensales en barra y mesa.
        </p>
      </div>

      <div class="timeline-card">
        <div class="timeline-header">
          <span class="timeline-role">Atención al Público y Asesor de Ventas</span>
          <span class="timeline-location">El Tigre, Anzoátegui</span>
        </div>
        <div class="timeline-company">Tropas Sport's</div>
        <p class="timeline-desc">
          Asesoramiento directo y personalizado sobre productos deportivos, asegurando una experiencia óptima de compra y soporte en el control de mercancía en piso de venta.
        </p>
      </div>

      <div class="timeline-card">
        <div class="timeline-header">
          <span class="timeline-role">Atención al Cliente y Mesero</span>
          <span class="timeline-location">Barinas, Barinitas</span>
        </div>
        <div class="timeline-company">Atípico Café & Bar</div>
        <p class="timeline-desc">
          Servicio dinámico de atención a mesas, manteniendo altos estándares de hospitalidad, pulcritud, rapidez y cortesía en entorno de alto flujo de clientes.
        </p>
      </div>

      <div class="timeline-card">
        <div class="timeline-header">
          <span class="timeline-role">Almacenista, Perifoneador y Atención al Cliente</span>
          <span class="timeline-location">Valencia, Tinaquillo</span>
        </div>
        <div class="timeline-company">Inversiones Maralfri</div>
        <p class="timeline-desc">
          Control físico de inventarios, gestión de bodega, estibado seguro y promoción activa de productos y servicios mediante perifoneo comercial dinámico.
        </p>
      </div>

      <div class="timeline-card">
        <div class="timeline-header">
          <span class="timeline-role">Auxiliar Florista, Creador de Detalles y Atención</span>
          <span class="timeline-location">Acacías, Meta, Colombia</span>
        </div>
        <div class="timeline-company">Floristería María José</div>
        <p class="timeline-desc">
          Confección de arreglos florales, diseño de detalles creativos personalizados y atención orientada a la satisfacción y fidelización de la clientela.
        </p>
      </div>

    </div>
  </section>

  <!-- Sección: Contacto Directo -->
  <section id="contacto" class="section-wrap" style="background: #ffffff; max-width: 100%; border-top: 1px solid var(--border-color);">
    <div style="max-width: 1050px; margin: 0 auto;">
      <div class="section-header-center">
        <span class="section-tag">Comunicación</span>
        <h2 class="section-title-large">Vías de Contacto Directo</h2>
      </div>

      <div class="contact-grid-boxes">
        <!-- WhatsApp -->
        <a class="contact-card whatsapp-card" href="https://wa.me/584221110096?text=Hola%20Ignacio,%20vi%20tu%20perfil%20web%20y%20me%20gustar%C3%ADa%20conversar%20contigo." target="_blank" rel="noopener noreferrer">
          <div class="contact-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          </div>
          <span class="contact-card-label">WhatsApp</span>
          <span class="contact-card-val">+58 0422-1110096</span>
        </a>

        <!-- Teléfono -->
        <a class="contact-card" href="tel:04221110096">
          <div class="contact-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          </div>
          <span class="contact-card-label">Teléfono Directo</span>
          <span class="contact-card-val">0422-1110096</span>
        </a>

        <!-- Correo Electrónico -->
        <a class="contact-card" href="mailto:ignacio.labrador.rodriguez@gmail.com">
          <div class="contact-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
          </div>
          <span class="contact-card-label">Correo Electrónico</span>
          <span class="contact-card-val" style="font-size: 13px;">ignacio.labrador.rodriguez@gmail.com</span>
        </a>

        <!-- Sitio Web / Vercel -->
        <a class="contact-card web-card" href="https://ignacio-labrador.vercel.app/" target="_blank" rel="noopener noreferrer">
          <div class="contact-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          </div>
          <span class="contact-card-label">Sitio Web / Portafolio</span>
          <span class="contact-card-val" style="font-size: 13px; color: var(--accent);">ignacio-labrador.vercel.app</span>
        </a>

        <!-- Documento de Identidad -->
        <div class="contact-card" style="cursor: default;">
          <div class="contact-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><line x1="15" y1="8" x2="17" y2="8"></line><line x1="15" y1="12" x2="17" y2="12"></line><line x1="7" y1="16" x2="17" y2="16"></line></svg>
          </div>
          <span class="contact-card-label">Cédula de Identidad</span>
          <span class="contact-card-val">C.I.: 29.698.769</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <p>&copy; 2026 Ignacio Labrador &bull; Todos los derechos reservados. Diseñado para postulaciones profesionales y servicios técnicos.</p>
  </footer>

  <!-- Botón Flotante de WhatsApp -->
  <a class="floating-whatsapp" href="https://wa.me/584221110096?text=Hola%20Ignacio,%20vi%20tu%20perfil%20web%20y%20me%20gustar%C3%ADa%20conversar%20contigo." target="_blank" rel="noopener noreferrer" title="Escríbeme por WhatsApp">
    <span class="whatsapp-tooltip">¿Conversamos por WhatsApp?</span>
    <svg viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
  </a>

  <!-- Modal Interactivo para previsualizar el Currículum Oficial -->
  <div id="cv-modal" class="modal-overlay" onclick="cerrarModalAfuera(event)">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title">Currículum Vitae Oficial &bull; Ignacio Labrador</div>
        <div class="modal-actions">
          <a class="modal-btn modal-btn-download" href="curriculum_ignacio_labrador.pdf" download="Curriculum_Ignacio_Labrador.pdf">
            Descargar PDF
          </a>
          <a class="modal-btn" href="curriculum.html" target="_blank" style="background:#0f172a; color:#fff;">
            Abrir Versión Imprimible
          </a>
          <button class="modal-btn modal-btn-close" onclick="cerrarModalCV()">✕</button>
        </div>
      </div>
      <div class="modal-body">
        <iframe class="modal-iframe" src="curriculum.html" title="Currículum Vitae Ignacio Labrador"></iframe>
      </div>
    </div>
  </div>

  <script>
    function abrirModalCV() {{
      document.getElementById('cv-modal').classList.add('open');
      document.body.style.overflow = 'hidden';
    }}

    function cerrarModalCV() {{
      document.getElementById('cv-modal').classList.remove('open');
      document.body.style.overflow = 'auto';
    }}

    function cerrarModalAfuera(e) {{
      if (e.target.id === 'cv-modal') {{
        cerrarModalCV();
      }}
    }}
  </script>

</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated modern portfolio landing page index.html with Vercel link successfully!')
