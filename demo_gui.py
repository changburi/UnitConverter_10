"""UnitConverter_10 최소 GUI 데모 — 숫자 검증 · 단위 변환 시각 확인."""

from __future__ import annotations

import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.control.solver import solve
from src.control.validation import ValidationError, validate, validate_number
from src.entity.constants import SUPPORTED_UNITS


class UnitConverterDemo(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("UnitConverter_10 — GUI Demo")
        self.resizable(False, False)
        self._build_widgets()

    def _build_widgets(self) -> None:
        pad = {"padx": 8, "pady": 6}

        frm = ttk.Frame(self, padding=12)
        frm.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frm, text="숫자 (value)").grid(row=0, column=0, sticky="w", **pad)
        self.value_entry = ttk.Entry(frm, width=24)
        self.value_entry.grid(row=0, column=1, **pad)
        self.value_entry.insert(0, "2.5")

        ttk.Label(frm, text="원본 단위").grid(row=1, column=0, sticky="w", **pad)
        self.unit_var = tk.StringVar(value="meter")
        unit_box = ttk.Combobox(
            frm,
            textvariable=self.unit_var,
            values=list(SUPPORTED_UNITS),
            state="readonly",
            width=21,
        )
        unit_box.grid(row=1, column=1, **pad)

        btn_row = ttk.Frame(frm)
        btn_row.grid(row=2, column=0, columnspan=2, **pad)
        ttk.Button(btn_row, text="숫자 검증", command=self._on_validate_number).pack(
            side=tk.LEFT, padx=4
        )
        ttk.Button(btn_row, text="단위 변환", command=self._on_convert).pack(
            side=tk.LEFT, padx=4
        )

        ttk.Label(frm, text="결과").grid(row=3, column=0, sticky="nw", **pad)
        self.output = tk.Text(frm, width=48, height=8, state=tk.DISABLED)
        self.output.grid(row=3, column=1, **pad)

        hint = (
            "숫자 검증: E002/E005 (control)\n"
            "단위 변환: meter · feet · yard 전체 출력 (entity SSOT)"
        )
        ttk.Label(frm, text=hint, foreground="gray").grid(
            row=4, column=0, columnspan=2, sticky="w", **pad
        )

    def _set_output(self, text: str) -> None:
        self.output.configure(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)
        self.output.configure(state=tk.DISABLED)

    def _on_validate_number(self) -> None:
        value_str = self.value_entry.get()
        result = validate_number(value_str)
        if isinstance(result, ValidationError):
            self._set_output(f"[{result.code}] {result.message}")
            messagebox.showwarning("숫자 검증 실패", result.message)
            return
        self._set_output(f"OK — 유효한 숫자: {result}")

    def _on_convert(self) -> None:
        unit = self.unit_var.get()
        value_str = self.value_entry.get()
        line = f"{unit}:{value_str}"
        validated = validate(line)
        if isinstance(validated, ValidationError):
            self._set_output(f"[{validated.code}] {validated.message}")
            messagebox.showerror("변환 실패", validated.message)
            return
        self._set_output(solve(validated))


def main() -> None:
    app = UnitConverterDemo()
    app.mainloop()


if __name__ == "__main__":
    main()
