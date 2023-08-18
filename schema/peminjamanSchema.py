from marshmallow import Schema, fields, validate

class peminjamanSchema(Schema):
    id = fields.String(dump_only=True)
    nama = fields.String(required=True)
    judul_buku = fields.String(required=True)
    tanggal_peminjaman = fields.String(required=True)
    tanggal_pengembalian = fields.String(required=True)

    
    class Meta:
            strict = True