{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  name = "star-wars-text-shell";

  packages = with pkgs; [
    python314
    inotify-tools
  ];
}
