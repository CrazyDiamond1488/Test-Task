from flask import Flask, request, jsonify

app = Flask(__name__)

# Список для хранения объектов
stored_objects = []

# Метод 1: Сохранение объекта в формате JSON
@app.route('/test', methods=['POST'])
def store_object():
    data = request.get_json()
    stored_objects.append(data)
    app.logger.info("Сервер получил данные: %s", data)
    return jsonify({'"Объект успешно сохранен'}), 201

# Метод 2: Удаление объекта по заданному текстовому полю
@app.route('/delete/<field_value>', methods=['DELETE'])
def delete_object(field_value):
    global stored_objects
    stored_objects = [obj for obj in stored_objects if obj.get('field_to_match') != field_value]
    return jsonify({'Объект(ы) успешно удален(ы)'}), 200

# Метод 3: Получение объекта в формате XML
@app.route('/get_xml', methods=['GET'])
def get_xml_object():

    data = stored_objects[0]
    xml_data = "<object>"
    for key, value in data.items():
        xml_data += f"<{key}>{value}</{key}>"
    xml_data += "</object>"
    return xml_data, 200, {'Content-Type': 'application/xml'}

# Метод 4: Получение подобъекта из массива подобъектов в формате JSON
@app.route('/get_json/<int:index>', methods=['GET'])
def get_json_subobject(index):
    data = stored_objects[0]['sub_objects'][index]
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)