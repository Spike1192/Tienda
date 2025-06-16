from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer,SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from io import BytesIO
from flask import send_file, make_response
import os
import io

def generar_pdf_venta(nv, cliente, total, productos):
    buffer = BytesIO()

    now = datetime.now()
    fecha_str = now.strftime("%d-%m-%Y")
    hora_str = now.strftime("%H:%M:%S")

    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    styles = getSampleStyleSheet()

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "Variedades Doña Leidy")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 65, "Teléfono: 3151234578")
    c.drawString(50, height - 80, "Dirección: Calle 11 #11-85, Barrio San Judas")
    c.drawString(400, height - 50, f"Fecha: {fecha_str}")
    c.drawString(400, height - 65, f"Hora: {hora_str}")
    c.drawString(400, height - 80, f"N° Venta: {nv}")
    c.drawString(50, height - 110, f"Cliente: {cliente}")

    data = [["Cant.", "Descripción", "Precio Unit.", "Total"]]
    for prod in productos:
        cantidad = str(prod['cantidad'])
        descripcion = prod['producto']
        precio = f"${prod['precio']:.2f}"
        total_prod = f"${prod['cantidad'] * prod['precio']:.2f}"
        data.append([cantidad, descripcion, precio, total_prod])

    tabla = Table(data, colWidths=[60, 200, 100, 100])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))
    tabla.wrapOn(c, width, height)
    tabla.drawOn(c, 50, height - 300)

    c.drawString(400, height - 310 - (len(productos) * 20), f"Total a pagar: ${total:.2f}")
    c.drawCentredString(width / 2, 100, "Gracias por su compra")
    c.save()

    buffer.seek(0)
    return buffer

def generar_detalle_venta_pdf(venta, detalles):
    buffer = BytesIO()

    # Crear documento PDF con Platypus
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    normal_style = styles['Normal']

    # Encabezado
    elements.append(Paragraph("<b>Variedades Doña Leidy</b>", normal_style))
    elements.append(Paragraph("Teléfono: 3151234578", normal_style))
    elements.append(Paragraph("Dirección: Calle 11 #11-85, Barrio San Judas", normal_style))
    elements.append(Spacer(1, 12))

    # Título
    elements.append(Paragraph("Factura de Venta", title_style))

    # Información general
    elements.append(Paragraph(f"N° Venta: {venta['nv']}", normal_style))
    elements.append(Paragraph(f"Cliente: {venta['cliente']}", normal_style))
    elements.append(Paragraph(f"Fecha: {venta['fecha']}  Hora: {venta['hora']}", normal_style))

    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Detalles:", normal_style))
    elements.append(Spacer(1, 6))

    # Encabezados de tabla
    data = [["Producto", "Cantidad", "Precio Unitario", "Total"]]

    # Filas con datos de productos
    for d in detalles:
        cantidad = d['cantidad']
        precio = d['precio']
        total_producto = cantidad * precio
        data.append([
            d['producto'],
            str(cantidad),
            f"${precio:.2f}",
            f"${total_producto:.2f}"
        ])

    # Crear tabla
    table = Table(data, colWidths=[200, 80, 100, 100])

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (1,1), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ])


    
    table.setStyle(style)

    elements.append(table)

    elements.append(Paragraph(f"Total: ${venta['total']:.2f}", normal_style))

    doc.build(elements)

    buffer.seek(0)

    # Enviar el PDF para que se abra en el navegador
    response = make_response(buffer.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'inline; filename=venta_{venta["nv"]}.pdf'

    return response


def generar_ventas_por_fecha(ventas, fecha_desde, fecha_hasta):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(200, 770, f"Reporte Mensual de Ventas")
    p.drawString(180, 755, f"Desde: {fecha_desde}  Hasta: {fecha_hasta}")

    y = 720
    p.drawString(40, y, "Nv")
    p.drawString(80, y, "Cliente")
    p.drawString(250, y, "Total")
    p.drawString(320, y, "Fecha")
    p.drawString(400, y, "Hora")
    y -= 20

    for v in ventas:
        p.drawString(40, y, str(v[0]))
        p.drawString(80, y, v[1])
        p.drawString(250, y, f"${v[2]:.2f}")
        p.drawString(320, y, v[3].strftime("%Y-%m-%d"))
        p.drawString(400, y, v[4])
        y -= 18
        if y < 50:
            p.showPage()
            y = 750

    p.save()
    buffer.seek(0)

    return make_response(buffer.getvalue(), {
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'inline; filename="reporte_mensual.pdf"'
    })