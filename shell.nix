let
  sources = import ./nix/sources.nix;
  pkgs = import ./nix/nixpkgs.nix { };
  cargoNix = pkgs.callPackage sources.cargo-nix { };
in pkgs.mkShell {
  buildInputs = [
    pkgs.nixfmt
    pkgs.niv
    cargoNix
    pkgs.python3
    pkgs.python3Packages.requests
    pkgs.python3Packages.beautifulsoup4
  ];
}
