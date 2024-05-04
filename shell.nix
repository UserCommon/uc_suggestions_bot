{ pkgs, lib, stdenv, ... }:

let
  pythonPackages = pkgs.python3Packages;
in
pkgs.mkShell {
  shellHook = ''
    alias run='python src/main.py'
    source .env
  '';

  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      aiogram
      python-dotenv
    ]))
  ];
}
