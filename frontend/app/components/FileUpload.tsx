"use client"; // クライアントコンポーネントとして指定

import { useState } from "react";

const FileUpload = () => {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("ファイルを選択してください。");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/uploadfile/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        setMessage("アップロード成功！");
      } else {
        setMessage("アップロード失敗...");
      }
    } catch (error) {
      console.log("エラー:", error);
      console.error("エラー:", error);
      setMessage("サーバーエラー");
    }
  };

  return (
    <div className="p-4 border rounded-lg shadow-md w-96">
      <input type="file" onChange={handleFileChange}
      className="border-2 border-gray-300 p-2 rounded-md mb-2 hover:bg-gray-200 transition-colors duration-200"
      />
      <button 
        onClick={handleUpload} 
        className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors duration-200"
      >
        アップロード
      </button>
      {message && <p className="mt-2">{message}</p>}
    </div>
  );
};

export default FileUpload;
