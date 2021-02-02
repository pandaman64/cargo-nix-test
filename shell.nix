let
  sources = import ./nix/sources.nix;
  pkgs = import ./nix/nixpkgs.nix { };
  cargoNix = pkgs.callPackage sources.cargo-nix { };
in pkgs.mkShell { buildInputs = [ pkgs.nixfmt cargoNix pkgs.python3 ]; }
