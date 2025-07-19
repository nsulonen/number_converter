{ pkgs, config, ... }:

{
  languages.python = {
    enable = true;

    venv.enable = true;
    venv.requirements = ''
      flask
    '';
  };
}
