from flask import Flask, jsonify, request

app = Flask(__name__)

class BilanganOperasiController:
    
    @staticmethod
    def createBilanganSegitiga():
        body_input = request.form
        
        if not body_input:
            return jsonify({'status_code': 400, 'message': "Input tidak ditemukan"})
        
        input_bil_value = body_input.get('input_bil')
        
        if not input_bil_value:
            return jsonify({'status_code': 400, 'message': "Input tidak boleh kosong"})
        
        try:
     
            number = int(input_bil_value)
            
            def generate_triangle(number):
                str_num = str(number)
                length = len(str_num)
                triangle = []
                for i in range(1, length + 1):
                    current_digit = str_num[i-1]
                    triangle.append(current_digit + '0' * (i-1))
                return triangle
            
            result = generate_triangle(number)
            
            return jsonify({'status_code': 200, 'message': "Berhasil", 'result': result})
        
        except ValueError:
            return jsonify({'status_code': 400, 'message': "Input harus berupa angka yang valid."})
    
    @staticmethod
    def createBilanganGanjil():
        body_input = request.form
        
        if not body_input:
            return jsonify({'status_code': 400, 'message': "Input tidak ditemukan"})
        
        input_bil_value = body_input.get('input_bil')
        
        if not input_bil_value:
            return jsonify({'status_code': 400, 'message': "Input tidak boleh kosong"})
        
        try:
            bil_len = int(input_bil_value)
            bil_ganjil = [num for num in range(bil_len + 1) if num % 2 != 0]
            
            return jsonify({'status_code': 200, 'message': f"Berhasil", 'result': bil_ganjil})
        
        except ValueError:
            return jsonify({'status_code': 400, 'message': "Input harus berupa angka yang valid."})
    
    @staticmethod
    def createBilanganPrima():
        body_input = request.form
        
        if not body_input:
            return jsonify({'status_code': 400, 'message': "Input tidak ditemukan"})
        
        input_bil_value = body_input.get('input_bil')
        
        if not input_bil_value:
            return jsonify({'status_code': 400, 'message': "Input tidak boleh kosong"})
        
        try:
            bil_len = int(input_bil_value)
            bil_prima_arr = [num for num in range(2, bil_len + 1) if BilanganOperasiController.is_bil_prima(num)]
            
            return jsonify({'status_code': 200, 'message': f"Berhasil", 'result': bil_prima_arr})
        
        except ValueError:
            return jsonify({'status_code': 400, 'message': "Input harus berupa angka yang valid."})
    
    @staticmethod
    def is_bil_prima(angka):
        if angka < 2:
            return False
        for data in range(2, int(angka ** 0.5) + 1):
            if angka % data == 0:
                return False
        return True