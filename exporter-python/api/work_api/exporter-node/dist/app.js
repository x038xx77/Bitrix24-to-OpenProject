"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// app.ts
const express_1 = __importDefault(require("express"));
const axios_1 = __importDefault(require("axios"));
const express_fileupload_1 = __importDefault(require("express-fileupload"));
const fs = __importStar(require("fs"));
const form_data_1 = __importDefault(require("form-data"));
const app = (0, express_1.default)();
const PORT = 8090;
app.use((0, express_fileupload_1.default)());
// Endpoint для отправки запроса
app.get('/start', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const metadata = { fileName: 'iAmage-(68).png' };
        const file = 'test_example.txt';
        // Создаем FormData и добавляем метаданные и файл
        const formData = new form_data_1.default();
        formData.append('metadata', JSON.stringify(metadata));
        formData.append('file', fs.createReadStream(file), { filename: 'test_example.txt' });
        // Отправляем POST-запрос на /api/v3/work_packages/49/attachments
        const response = yield axios_1.default.post('http://localhost:8080/api/v3/work_packages/49/attachments', formData, {
            headers: Object.assign({}, formData.getHeaders()),
        });
        // Обрабатываем ответ от сервера
        console.log(response.data);
        // Вернуть ответ клиенту
        res.status(200).json({ message: 'Request sent successfully' });
    }
    catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}));
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
