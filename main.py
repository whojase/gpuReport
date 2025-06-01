import GPUtil
from fpdf import FPDF
import datetime

class System:
    def __init__(self):
        self.gpu_util = None
        
    def generate_gpu_report(self):
        self.gpu_util = GPUtil.getGPUs()
        
        if not self.gpu_util:
            print('Error: GPU not found')
            return
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size = 12)
        
        pdf.cell(200, 10, txt = 'GPU Status Report', ln = 1, align = 'C')
        pdf.cell(200, 10, txt = f'Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', ln = 2, align = 'C')
        pdf.ln(10)
        
        for gpu in self.gpu_util:
            pdf.multi_cell(0, 10, (
                f'GPU ID: {gpu.id}\n'
                f'Name: {gpu.name}\n'
                f'Download: {gpu.load*100:.2f}%\n'
                f'Used Memory: {gpu.memoryUtil*100:.2f}%\n'
                f'Temp: {gpu.temperature:.2f}°C'
            ))
            pdf.ln(5)
            pdf.cell(0, 0, txt = '-' * 50, ln = 1)
            pdf.ln(5)
    
        filename = f'gpu_report_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        pdf.output(filename)
        print(f'Report saved how {filename}')

if __name__ == '__main__':
    sys = System()
    sys.generate_gpu_report()