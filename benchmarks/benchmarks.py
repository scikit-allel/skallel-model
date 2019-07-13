import numpy as np
import dask.array as da
from skallel_tensor import numpy_backend, dask_backend


class TimeGenotypes3D:
    """Timing benchmarks for genotypes 3D functions."""

    def setup(self):
        self.data = np.random.randint(-1, 4, size=(10000, 1000, 2), dtype="i1")
        self.data_dask = da.from_array(self.data, chunks=(1000, 200, 2))

    def time_locate_called_numpy(self):
        numpy_backend.genotypes_3d_locate_called(self.data)

    def time_locate_called_dask(self):
        dask_backend.genotypes_3d_locate_called(self.data_dask).compute()

    def time_locate_missing_numpy(self):
        numpy_backend.genotypes_3d_locate_missing(self.data)

    def time_locate_missing_dask(self):
        dask_backend.genotypes_3d_locate_missing(self.data_dask).compute()

    def time_locate_hom_numpy(self):
        numpy_backend.genotypes_3d_locate_hom(self.data)

    def time_locate_hom_dask(self):
        dask_backend.genotypes_3d_locate_hom(self.data_dask).compute()

    def time_locate_het_numpy(self):
        numpy_backend.genotypes_3d_locate_het(self.data)

    def time_locate_het_dask(self):
        dask_backend.genotypes_3d_locate_het(self.data_dask).compute()

    def time_locate_call_numpy(self):
        numpy_backend.genotypes_3d_locate_call(
            self.data, np.array([0, 1], dtype="i1")
        )

    def time_locate_call_dask(self):
        dask_backend.genotypes_3d_locate_call(
            self.data_dask, np.array([0, 1], dtype="i1")
        ).compute()

    def time_count_alleles_numpy(self):
        numpy_backend.genotypes_3d_count_alleles(self.data, max_allele=3)

    def time_count_alleles_dask(self):
        dask_backend.genotypes_3d_count_alleles(
            self.data_dask, max_allele=3
        ).compute()

    def time_to_allele_counts_numpy(self):
        numpy_backend.genotypes_3d_to_allele_counts(self.data, max_allele=3)

    def time_to_allele_counts_dask(self):
        dask_backend.genotypes_3d_to_allele_counts(
            self.data_dask, max_allele=3
        ).compute()

    def time_to_allele_counts_melt_numpy(self):
        numpy_backend.genotypes_3d_to_allele_counts_melt(
            self.data, max_allele=3
        )

    def time_to_allele_counts_melt_dask(self):
        dask_backend.genotypes_3d_to_allele_counts_melt(
            self.data_dask, max_allele=3
        ).compute()


class TimeAlleleCounts2D:
    """Timing benchmarks for allele counts 2D functions."""

    def setup(self):
        self.data = np.random.randint(0, 100, size=(10000000, 4), dtype="i4")
        self.data_dask = da.from_array(self.data, chunks=(100000, -1))

    def time_to_frequencies(self):
        numpy_backend.allele_counts_2d_to_frequencies(self.data)

    def time_allelism(self):
        numpy_backend.allele_counts_2d_allelism(self.data)

    def time_max_allele(self):
        numpy_backend.allele_counts_2d_max_allele(self.data)

    def time_locate_variant(self):
        numpy_backend.allele_counts_2d_locate_variant(self.data)

    def time_locate_non_variant(self):
        numpy_backend.allele_counts_2d_locate_variant(self.data)

    def time_locate_segregating(self):
        numpy_backend.allele_counts_2d_locate_segregating(self.data)


class TimeAlleleCounts3D:
    """Timing benchmarks for allele counts 3D functions."""

    def setup(self):
        gt = np.random.randint(-1, 4, size=(10000, 1000, 2), dtype="i1")
        self.data = numpy_backend.genotypes_3d_to_allele_counts(
            gt, max_allele=3
        )
        self.data_dask = da.from_array(self.data, chunks=(1000, 200, -1))

    def time_locate_called_numpy(self):
        numpy_backend.allele_counts_3d_locate_called(self.data)

    # def time_locate_called_dask(self):
    #     dask_backend.allele_counts_3d_locate_called(self.data_dask).compute()

    def time_locate_missing_numpy(self):
        numpy_backend.allele_counts_3d_locate_missing(self.data)

    # def time_locate_missing_dask(self):
    #     dask_backend.allele_counts_3d_locate_missing(self.data_dask).compute()

    def time_locate_hom_numpy(self):
        numpy_backend.allele_counts_3d_locate_hom(self.data)

    # def time_locate_hom_dask(self):
    #     dask_backend.allele_counts_3d_locate_hom(self.data_dask).compute()

    def time_locate_het_numpy(self):
        numpy_backend.allele_counts_3d_locate_het(self.data)

    # def time_locate_het_dask(self):
    #     dask_backend.allele_counts_3d_locate_het(self.data_dask).compute()

    # def time_locate_call_numpy(self):
    #     numpy_backend.allele_counts_3d_locate_call(
    #         self.data, np.array([0, 1], dtype="i1")
    #     )

    # def time_to_frequencies(self):
    #     numpy_backend.allele_counts_3d_to_frequencies(self.data)

    def time_allelism(self):
        numpy_backend.allele_counts_3d_allelism(self.data)

    # def time_max_allele(self):
    #     numpy_backend.allele_counts_3d_max_allele(self.data)

    # def time_locate_variant(self):
    #     numpy_backend.allele_counts_3d_locate_variant(self.data)

    # def time_locate_non_variant(self):
    #     numpy_backend.allele_counts_3d_locate_variant(self.data)

    # def time_locate_segregating(self):
    #     numpy_backend.allele_counts_3d_locate_segregating(self.data)
