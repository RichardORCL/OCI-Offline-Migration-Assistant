"""Product naming and OCI label prefixes for the OCI Offline Migration Assistant."""

from __future__ import annotations

PRODUCT_NAME = "OCI Offline Migration Assistant"
PRODUCT_VM_NAME = "OCI Offline Migration Assistant VM"
GITHUB_OWNER = "RichardORCL"
GITHUB_REPO = "OCI-Offline-Migration-Assistant"
SOURCE_GIT_URL = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}.git"
STACK_ZIP_FILENAME = "oci-offline-migration-assistant-stack.zip"
DEFINED_TAG_NAMESPACE = "OfflineMigrationAssistant"

# Internal compatibility prefix for freeform tags, seed bucket defaults, staging paths, etc.
PREFIX = "oci-umt"


def tag_key(suffix: str = "") -> str:
    """Freeform tag key: ``oci-umt`` or ``oci-umt-<suffix>``."""
    return f"{PREFIX}-{suffix}" if suffix else PREFIX


TAG_CONSOLE = tag_key()
TAG_CONSOLE_VALUE = "console"
TAG_JOB = tag_key("job")
TAG_DISK_INDEX = tag_key("disk-index")
TAG_SEED = tag_key("seed")
TAG_FIRMWARE = tag_key("firmware")
TAG_OS = tag_key("os")
TAG_SECURE_BOOT = tag_key("secure-boot")
TAG_LAUNCH_MODE = tag_key("launch-mode")
ISO_TAG = tag_key("iso")
ISO_SOURCE_TAG = tag_key("iso-source")
ISO_ETAG_TAG = tag_key("iso-etag")
OVA_TAG = tag_key("ova")
OVA_SOURCE_TAG = tag_key("ova-source")
OVA_ETAG_TAG = tag_key("ova-etag")
TAG_SOURCE_OVA = tag_key("source-ova")
OVA_DISPLAY_PREFIX = f"{PREFIX}-ova"
TAG_SOURCE_VM = tag_key("source-vm")
TAG_SOURCE_MOID = tag_key("source-moid")
TAG_SOURCE_VM_DETAILS = tag_key("source-vm-details")
TAG_SOURCE_VCENTER = tag_key("source-vcenter")
TAG_SOURCE_ESXI_HOST = tag_key("source-esxi-host")
TAG_SOURCE_AZURE = tag_key("source-azure")
TAG_SOURCE_GCP = tag_key("source-gcp")
TAG_SOURCE_AWS = tag_key("source-aws")
TAG_SOURCE_OLVM = tag_key("source-olvm")
TAG_SOURCE_HYPERV = tag_key("source-hyperv")
TAG_SOURCE_NUTANIX = tag_key("source-nutanix")
TAG_SOURCE_PROXMOX = tag_key("source-proxmox")
TAG_SOURCE_ISO = tag_key("source-iso")
TAG_SOURCE_DETAILS = tag_key("source-details")

SEED_BUCKET_DEFAULT = f"{PREFIX}-seed-images"
SEED_DISPLAY_PREFIX = f"{PREFIX}-seed"
ISO_DISPLAY_PREFIX = f"{PREFIX}-iso"
