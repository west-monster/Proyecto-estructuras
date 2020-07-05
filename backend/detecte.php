<?php
    header("Access-Control-Allow-Origin: *");
    header("Content-Type: application/json; charset=UTF-8");
    header('Access-Control-Allow-Methods: POST');
    header('Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept, Authorization');
    $arRes = new stdClass();
    if (isset($_FILES['file']['tmp_name'])) {
        if (move_uploaded_file($_FILES['file']['tmp_name'], "C:/xampp/htdocs/e2/backend/".$_FILES['file']['name'])) {
            $command = escapeshellcmd('python C:\xampp\htdocs\e2\backend\IA.py');
            $output = shell_exec($command);
            $output = str_replace("\r\n","",$output);
            $output = str_replace("'","\"",$output);
            $arRes->ans = json_decode($output);
            unlink("C:/xampp/htdocs/e2/backend/".$_FILES['file']['name']);
            $arRes->query = true;
        }else{
            $arRes->query = false;
        }
    }
    echo json_encode($arRes);
?>