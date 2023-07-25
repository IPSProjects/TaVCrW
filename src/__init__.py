import ipsuite as ips
import typing
import zntrack
import numpy as np
import pathlib
import tqdm
import ase
from ase.calculators.singlepoint import SinglePointCalculator

TYPE_MAPPING = {
    0: "Ta",
    1: "V",
    2: "Cr",
    3: "W",
}


class ReadNPZ(zntrack.Node):
    atoms: typing.List[ase.Atoms] = ips.fields.Atoms()
    directory: typing.Union[str, pathlib.Path] = zntrack.dvc.deps()
    regex: str = zntrack.zn.params("4comp.cfg_train*")

    def run(self):
        self.atoms = []
        for directory in tqdm.tqdm(pathlib.Path(self.directory).glob(self.regex)):
            for file in directory.glob("*"):
                with np.load(file) as data:
                    symbols = [TYPE_MAPPING[t] for t in data["types"]]
                    atoms = ase.Atoms(
                        symbols, cell=data["cell"], positions=data["pos"], pbc=True # with or without PBC ???
                    )
                    atoms.calc = SinglePointCalculator(
                        atoms,
                        energy=data["energy"][0],
                        forces=data["forces"],
                        stress=data["stress"],
                    )
                    self.atoms.append(atoms)
