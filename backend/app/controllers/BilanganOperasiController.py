from flask import Flask, jsonify, request

class BilanganOperasiController():
    
    @staticmethod
    def createBilanganSegitiga():
        body_input =request.form
        
        if not body_input:
            return jsonify({'status_code': 404, 'message': "Maaf ada error pada saat proses inputnya"})
        
        input_bil_value = body_input.get('input_bil')
        
        if not input_bil_value:
            return jsonify({'status_code': 404, 'message': "Maaf input anda masih kosong"})
        else:
            total_huruf = len(input_bil_value)
            final_bil = ''
            count_bil = 1
            # for data in total_huruf:
            #     if data == "0" :
            #         num_bil = data + "0"
            #     else:
                    
                 
            return jsonify({'status_code': 200, 'message': f"Test Memiliki Jumlah Panjang Bilangan Bulat {isinstance(input_bil_value, str)}"})
        
        
    staticmethod
    def createBilanganGanjil():
        body_input =request.form
        
        if not body_input:
            return jsonify({'status_code': 404, 'message': "Maaf ada error pada saat proses inputnya"})
        
        input_bil_value = body_input.get('input_bil')
        
        if not input_bil_value:
            return jsonify({'status_code': 404, 'message': "Maaf input anda masih kosong"})
        else:
            bil_len = input_bil_value
            bil_arr = []
            bil_ganjil = []
            for data in range(0, int(bil_len) + 1):
                bil_arr.append(data)
            
            for data2 in bil_arr:
                # if data2 % 2 == 1:
                bilangan_found = 0
                if data2 % 2 == 1:
                    bilangan_found = data2
                    
                if bilangan_found != 0:
                    bil_ganjil.append(bilangan_found)
    
            
            return jsonify({'status_code': 200, 'message': f"Test Memiliki bilangan ganjil {bil_ganjil}"})
        
    staticmethod
    def createBilanganGenap():
        body_input =request.form
        
        if not body_input:
            return jsonify({'status_code': 404, 'message': "Maaf ada error pada saat proses inputnya"})
        
        input_bil_value = body_input.get('input_bil')
        
        if not input_bil_value:
            return jsonify({'status_code': 404, 'message': "Maaf input anda masih kosong"})
        else:
            bil_len = input_bil_value
            bil_arr = []
            bil_genap = []
            for data in range(0, int(bil_len) + 1):
                bil_arr.append(data)
            
            for data2 in bil_arr:
                # if data2 % 2 == 1:
                bilangan_found = 0
                if data2 % 2 == 0:
                    bilangan_found = data2
                    
                if bilangan_found != 0:
                    bil_genap.append(bilangan_found)
    
            
            return jsonify({'status_code': 200, 'message': f"Test Memiliki bilangan ganjil {bil_genap}"})